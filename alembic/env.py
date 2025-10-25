from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config
from alembic import context
import asyncio

# Importer la config et Base
from src.config import settings
from src.database import Base

# Importer TOUS les models pour que Alembic les détecte
from src.models.users import User
from src.models.products import Product
from src.models.product_images import ProductImage
from src.models.orders import Order
from src.models.categories import Category
from src.models.brands import Brand
from src.models.attributes import Attribute
from src.models.associations import order_products, product_attributes

# this is the Alembic Config object
config = context.config

# Interpréter le fichier de config pour le logging Python
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata des models
target_metadata = Base.metadata

# Définir l'URL de la DB depuis settings
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """Run migrations in 'online' mode."""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()