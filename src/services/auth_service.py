from typing import Optional

from fastapi import Depends
from src.repositories.user_repo import UserRepository
from src.utils.security import verify_password, create_access_token
from src.database import Database, get_db
from src.schemas.auth import TokenResponse
from src.utils.exceptions import UnauthorizedException

class AuthService:
    def __init__(self, db: Database):
        self.db = db

    async def authenticate_user(self, email: str, password: str) -> TokenResponse:
        """Authentifie un utilisateur et retourne un token"""
        user = await UserRepository(self.db).get_by_email(email)

        if not user or not verify_password(password, user.password):
            raise UnauthorizedException("Email ou mot de passe incorrect")
        
        # Créer le token JWT
        token_data = {
            "sub": str(user.id),
            "email": user.email,
            "role": user.role.value
        }
        access_token = create_access_token(token_data)
        
        return TokenResponse(access_token=access_token)
    

def get_auth_service(db: Database = Depends(get_db)) -> AuthService:
    return AuthService(db)