from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_db
from src.schemas.auth import LoginRequest, TokenResponse
from src.schemas.user import UserOut
from src.services.auth_service import AuthService, get_auth_service
from src.middleware.auth_middleware import get_current_user
from src.utils.exceptions import LemoServiceException
from src.utils.logging_config import logger

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=TokenResponse)
async def login(
    credentials: LoginRequest,
    auth_service: AuthService = Depends(get_auth_service),
):
    """Connexion admin"""
    try:
        return await auth_service.authenticate_user(
            credentials.email, credentials.password
        )
    except LemoServiceException as e:
        logger.warning(f"Failed login attempt for email: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/me", response_model=UserOut)
async def get_me(current_user=Depends(get_current_user)):
    """Récupère les infos de l'utilisateur connecté"""
    try:
        return current_user
    except LemoServiceException as e:
        logger.error(f"Failed to get current user: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))
