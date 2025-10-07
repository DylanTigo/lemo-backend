import logging
import asyncio
from random import random
from typing import AsyncGenerator, Callable, Coroutine, Dict, Any, Optional
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import QueuePool
from sqlalchemy import text, event
from sqlalchemy.exc import DisconnectionError, OperationalError, TimeoutError
from src.config import settings
import time

logger = logging.getLogger(__name__)

Base = declarative_base()


class DatabaseError(Exception):
    """Custom database exception"""

    pass


class Database:
    def __init__(self):
        # Enhanced connection pool configuration
        self.engine = create_async_engine(
            settings.DATABASE_URL,
            future=True,
            pool_size=settings.DB_POOL_SIZE,
            max_overflow=settings.DB_MAX_OVERFLOW,
            pool_timeout=settings.DB_POOL_TIMEOUT,
            pool_recycle=3600,  # Recycle connections every hour
            pool_pre_ping=True,  # Validate connections before use
            # Dialect-specific arguments
            connect_args=(
                {
                    "command_timeout": 60,
                    "server_settings": {
                        "application_name": "notification_service",
                    },
                }
                if "postgresql" in settings.DATABASE_URL
                else {}
            ),
        )

        self.session_local = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
            class_=AsyncSession,
        )

        # Connection pool monitoring
        self._setup_pool_monitoring()

        # Health check cache
        self._last_health_check: Dict[str, Any] | None = None
        self._health_check_cache_duration = 30  # seconds

    def _setup_pool_monitoring(self):
        """Setup connection pool event monitoring."""
        # Use sync_engine for proper event handling with async engines
        sync_engine = self.engine.sync_engine

        @event.listens_for(sync_engine, "connect")
        def receive_connect(dbapi_connection, connection_record):
            logger.debug("New database connection established")

        @event.listens_for(sync_engine, "checkout")
        def receive_checkout(dbapi_connection, connection_record, connection_proxy):
            pool = self.engine.pool
            logger.debug(
                f"Connection checked out. Pool stats - Size: {pool.size()}, "
                f"Checked out: {pool.checkedout()}, Overflow: {pool.overflow()}"
            )

        @event.listens_for(sync_engine, "checkin")
        def receive_checkin(dbapi_connection, connection_record):
            logger.debug("Connection checked back in")

    async def initialize(self):
        """Initialize database with retry logic"""
        max_retries = 3
        retry_delay = 5

        for attempt in range(max_retries):
            try:
                async with self.engine.begin() as conn:
                    await conn.run_sync(Base.metadata.create_all)
                logger.info("Database initialized successfully")
                return
            except Exception as e:
                logger.error(
                    f"DB init failed (attempt {attempt + 1}/{max_retries}): {e}"
                )
                if attempt == max_retries - 1:
                    # Preserve original exception context
                    raise DatabaseError("Failed to initialize database") from e
                await asyncio.sleep(retry_delay)

    async def drop_tables(self):
        """Drop all database tables."""
        try:
            async with self.engine.begin() as conn:
                await conn.run_sync(Base.metadata.drop_all)
            logger.info("All tables dropped successfully")
        except Exception as e:
            # Preserve original exception context
            raise DatabaseError("Failed to drop tables") from e

    async def health_check(self) -> Dict[str, Any]:
        """Comprehensive health check with caching"""
        current_time = time.time()

        # Return cached result if recent
        if (
            self._last_health_check
            and current_time - self._last_health_check["timestamp"]
            < self._health_check_cache_duration
        ):
            return self._last_health_check

        health_status = {
            "timestamp": current_time,
            "status": "healthy",
            "pool_stats": {},
            "errors": [],
        }

        try:
            # Test basic connectivity
            async with self.engine.connect() as conn:
                await conn.execute(text("SELECT 1"))

            # Get pool statistics
            pool_stats = self.get_pool_stats()
            health_status["pool_stats"] = pool_stats

            # Check if pool is near capacity
            if pool_stats["total_capacity"] > 0:
                utilization = pool_stats["checked_out"] / pool_stats["total_capacity"]
                if utilization > 0.8:
                    health_status["errors"].append(
                        f"High pool utilization: {utilization:.2%}"
                    )

        except Exception as e:
            health_status["status"] = "unhealthy"
            health_status["errors"].append(str(e))
            logger.error(f"Database health check failed: {e}")

        self._last_health_check = health_status
        return health_status

    def get_pool_stats(self) -> Dict[str, int]:
        """Get current connection pool statistics."""
        pool = self.engine.pool
        return {
            "size": pool.size(),
            "checked_out": pool.checkedout(),
            "overflow": pool.overflow(),
            "total_capacity": pool.size() + pool.overflow(),
            "available": pool.size() + pool.overflow() - pool.checkedout(),
        }

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Context manager for sessions with robust error handling."""
        session: AsyncSession | None = None
        try:
            session = self.session_local()
            yield session
            await session.commit()
        except (DisconnectionError, OperationalError, TimeoutError) as e:
            logger.error(f"Database connection error: {e}")
            if session:
                await session.rollback()
            # Preserve original exception context
            raise DatabaseError("Database connection failed") from e
        except Exception:
            logger.error("An unexpected database error occurred", exc_info=True)
            if session:
                await session.rollback()
            raise  # Re-raise the original, unknown exception
        finally:
            if session:
                await session.close()

    async def execute_with_retry(
        self,
        operation: Callable[[AsyncSession], Coroutine],
        max_retries=3,
        retry_delay=1,
    ):
        """Execute a database operation with exponential backoff and jitter."""
        for attempt in range(max_retries):
            try:
                async with self.get_session() as session:
                    return await operation(session)
            except DatabaseError as e:
                logger.warning(
                    f"DB operation failed (attempt {attempt + 1}/{max_retries}): {e}"
                )
                if attempt == max_retries - 1:
                    raise
                # Added jitter to the backoff delay
                delay = (retry_delay * (2**attempt)) + random.uniform(0, 0.5)
                await asyncio.sleep(delay)

    async def close(self):
        """Close database connections gracefully."""
        logger.info("Closing database connections.")
        await self.engine.dispose()
        logger.info("Database connections closed successfully.")


# Global database instance
db = Database()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    return db


# Example usage with retry logic
async def safe_database_operation(operation_func):
    """Wrapper for database operations with automatic retry"""
    return await db.execute_with_retry(operation_func)
