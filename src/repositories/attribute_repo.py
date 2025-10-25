from typing import Optional, List
from sqlalchemy import select, func
from src.models.attributes import Attribute
from src.repositories.base import BaseRepository


class AttributeRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, Attribute)

    async def get_by_id(self, attribute_id: int) -> Optional[Attribute]:
        """Récupère un attribut par ID"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Attribute).where(Attribute.id == attribute_id)
            )
            return result.scalar_one_or_none()

    async def list_all(self) -> List[Attribute]:
        """Liste tous les attributs"""
        async with self.db.get_session() as session:
            result = await session.execute(select(Attribute).order_by(Attribute.name))
            return result.scalars().all()

    async def get_count(self) -> int:
        """Compte le nombre d'attributs"""
        async with self.db.get_session() as session:
            result = await session.execute(select(func.count(Attribute.id)))
            return result.scalar()

    async def create(self, attribute_data: dict) -> Attribute:
        """Crée un attribut"""
        async with self.db.get_session() as session:
            existing_attribute = await session.execute(
                select(Attribute).where(Attribute.name == attribute_data["name"])
            )
            if existing_attribute.scalar_one_or_none():
                return None
            attribute = Attribute(**attribute_data)
            session.add(attribute)
            await session.commit()
            await session.refresh(attribute)
            return attribute

    async def update(
        self, attribute_id: int, attribute_data: dict
    ) -> Optional[Attribute]:
        """Met à jour un attribut"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Attribute).where(Attribute.id == attribute_id)
            )
            attribute = result.scalar_one_or_none()

            if not attribute:
                return None

            for key, value in attribute_data.items():
                setattr(attribute, key, value)

            await session.commit()
            await session.refresh(attribute)
            return attribute

    async def delete(self, attribute_id: int) -> bool:
        """Supprime un attribut"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Attribute).where(Attribute.id == attribute_id)
            )
            attribute = result.scalar_one_or_none()
            if not attribute:
                return False
            await session.delete(attribute)
            await session.commit()
            return True
