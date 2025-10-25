from typing import Optional, List
from sqlalchemy import select, func
from src.models.brands import Brand
from src.repositories.base import BaseRepository

class BrandRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, Brand)
    
    async def get_by_id(self, brand_id: int) -> Optional[Brand]:
        """Récupère une marque par ID"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Brand).where(Brand.id == brand_id)
            )
            return result.scalar_one_or_none()
    
    async def get_by_name(self, name: str) -> Optional[Brand]:
        """Récupère une marque par nom"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Brand).where(Brand.name == name)
            )
            return result.scalar_one_or_none()
    
    async def list_all(self) -> List[Brand]:
        """Liste toutes les marques"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Brand).order_by(Brand.name)
            )
            return result.scalars().all()
    
    async def get_count(self) -> int:
        """Compte le nombre de marques"""
        async with self.db.get_session() as session:
            result = await session.execute(select(func.count(Brand.id)))
            return result.scalar()
    
    async def create(self, brand_data: dict) -> Brand:
        """Crée une marque"""
        async with self.db.get_session() as session:
            brand = Brand(**brand_data)
            session.add(brand)
            await session.commit()
            await session.refresh(brand)
            return brand
    
    async def update(self, brand_id: int, brand_data: dict) -> Optional[Brand]:
        """Met à jour une marque"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Brand).where(Brand.id == brand_id)
            )
            brand = result.scalar_one_or_none()
            
            if not brand:
                return None
            
            for key, value in brand_data.items():
                setattr(brand, key, value)
            
            await session.commit()
            await session.refresh(brand)
            return brand
    
    async def delete(self, brand_id: int) -> bool:
        """Supprime une marque"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Brand).where(Brand.id == brand_id)
            )
            brand = result.scalar_one_or_none()
            
            if not brand:
                return False
            
            await session.delete(brand)
            await session.commit()
            return True