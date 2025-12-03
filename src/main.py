import logging

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBearer
import uvicorn
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

print(f"Starting Lemo Backend with DATABASE_URL: {settings.DATABASE_URL}")
# Include API routers
app.include_router(api_router, prefix="/api/v1")

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def root():
    return """
    <html>
        <head>
            <title>Lemo API</title>
        </head>
        <body>
            <h1>Welcome to Lemo API</h1>
            <p>Choose an option:</p>
            <ul>
                <li><a href="/docs">Interactive API Documentation</a></li>
                <li><a href="/redoc">Redoc Documentation</a></li>
            </ul>
        </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
