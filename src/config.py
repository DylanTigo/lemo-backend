import os
from pathlib import Path

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Get the src directory path
SRC_DIR = Path(__file__).parent.parent
DOTENV = os.path.join(SRC_DIR, ".env")
DOTENV_PROD = os.path.join(SRC_DIR, ".env.prod")

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=(DOTENV, DOTENV_PROD),
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    PROJECT_NAME: str = "Lemo Backend"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "your_secret_key"

settings = Settings()