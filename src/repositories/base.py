from typing import Optional
from pydantic import EmailStr
from sqlalchemy.future import select
from src.database import Database


class BaseRepository:
    def __init__(self, db: Database, model):
        self.db = db
        self.model = model

    async def get_by_id(self, id: int):
        async with self.db.get_session() as session:
            query = select(self.model).where(self.model.id == id)
            result = await session.execute(query)
            return result.scalars().first()

    async def list_all(self):
        async with self.db.get_session() as session:
            query = select(self.model)
            result = await session.execute(query)
            return result.scalars().all()

    async def create(self, obj_data: dict):
        obj = self.model(**obj_data)
        async with self.db.get_session() as session:
            session.add(obj)
            await session.commit()
            await session.refresh(obj)
        return obj

    async def update(self, id: int, obj_data: dict):
        # Fetch and update within the same session to avoid detached instances
        async with self.db.get_session() as session:
            query = select(self.model).where(self.model.id == id)
            result = await session.execute(query)
            obj = result.scalars().first()
            if not obj:
                return None
            for key, value in obj_data.items():
                setattr(obj, key, value)
            await session.commit()
            await session.refresh(obj)
            return obj

    async def delete(self, id: int):
        async with self.db.get_session() as session:
            # Load the object within the same session before deleting
            query = select(self.model).where(self.model.id == id)
            result = await session.execute(query)
            obj = result.scalars().first()
            if not obj:
                return None
            await session.delete(obj)
            await session.commit()
            return obj
