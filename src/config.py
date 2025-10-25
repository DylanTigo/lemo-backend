import os
from pathlib import Path

from pydantic import Field, computed_field
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
    POSTGRES_DB_USER: str = ""
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB_HOST: str = ""
    POSTGRES_DB_PORT: int = 5432
    POSTGRES_DB_NAME: str = ""
    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20
    DB_POOL_TIMEOUT: int = 30

    PROJECT_NAME: str = "Lemo Backend"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "your_secret_key"

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        """
        This field is computed from the other Postgres fields at runtime.
        It will not be loaded from or stored in the environment directly.
        """
        return (
            f"postgresql+asyncpg://{self.POSTGRES_DB_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_DB_HOST}:"
            f"{self.POSTGRES_DB_PORT}/{self.POSTGRES_DB_NAME}"
        )

settings = Settings()