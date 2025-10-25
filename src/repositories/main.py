from typing import Optional
from pydantic import EmailStr
from sqlalchemy.future import select
from src.database import Database


class BaseRepository:
    def __init__(self, db: Database, model):
        self.db = db
        self.model = model

    async def get_by_id(self, id: int):
        query = select(self.model).where(self.model.id == id)
        result = await self.db.session.execute(query)
        return result.scalars().first()

    async def list_all(self):
        query = select(self.model)
        result = await self.db.session.execute(query)
        return result.scalars().all()

    async def create(self, obj_data: dict):
        obj = self.model(**obj_data)
        self.db.session.add(obj)
        await self.db.session.commit()
        await self.db.session.refresh(obj)
        return obj

    async def update(self, id: int, obj_data: dict):
        obj = await self.get_by_id(id)
        for key, value in obj_data.items():
            setattr(obj, key, value)
        self.db.session.add(obj)
        await self.db.session.commit()
        await self.db.session.refresh(obj)
        return obj

    async def delete(self, id: int):
        obj = await self.get_by_id(id)
        await self.db.session.delete(obj)
        await self.db.session.commit()
        return obj
