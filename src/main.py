import logging

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.security import HTTPBearer
from src.api import api_router
from fastapi.middleware.cors import CORSMiddleware
from src.config import settings, ORIGINS
from src.utils.logging_config import setup_logging
from src.database import Database
import os

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Setup logging configuration to filter health checks
    setup_logging()
    if os.getenv("ENVIRONMENT") != "test":
        database = Database()
        await database.initialize()
    yield
    if os.getenv("ENVIRONMENT") != "test":
        await database.close()


security_scheme = HTTPBearer()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(api_router, prefix="/api/v1")