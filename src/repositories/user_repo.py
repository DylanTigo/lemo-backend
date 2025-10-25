from typing import Optional
from sqlalchemy import select
from src.database import Database
from src.models.users import User
from src.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(db, User)

    async def get_by_email(self, email: str) -> Optional[User]:
        """Récupère un utilisateur par email"""
        async with self.db.get_session() as session:
            result = await session.execute(select(User).where(User.email == email))
            return result.scalar_one_or_none()
