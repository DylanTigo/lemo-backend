import os
from pathlib import Path

from pydantic import Field, computed_field
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

# Get the src directory path
SRC_DIR = Path(__file__).parent.parent
DOTENV = os.path.join(SRC_DIR, ".env")
DOTENV_PROD = os.path.join(SRC_DIR, ".env.prod")

ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000"]


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=(DOTENV, DOTENV_PROD),
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )
    JWT_SECRET_KEY: str = "lemo-backend"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 24 * 2

    POSTGRES_DB_USER: str = Field(..., env="POSTGRES_DB_USER")
    POSTGRES_PASSWORD: str = Field(..., env="POSTGRES_PASSWORD")
    POSTGRES_DB_HOST: str = Field(..., env="POSTGRES_DB_HOST")
    POSTGRES_DB_PORT: int = Field(5432, env="POSTGRES_DB_PORT")
    POSTGRES_DB_NAME: str = Field(..., env="POSTGRES_DB_NAME")
    DATABASE_URL: str = Field(None, env="DATABASE_URL")
    DB_POOL_SIZE: int = Field(10, env="DB_POOL_SIZE")
    DB_MAX_OVERFLOW: int = 20
    DB_POOL_TIMEOUT: int = 30

    PROJECT_NAME: str = "Lemo Backend"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "your_secret_key"

settings = Settings()
