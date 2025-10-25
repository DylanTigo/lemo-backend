from typing import Optional, List
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload
from src.models.categories import Category
from src.repositories.base import BaseRepository

class CategoryRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, Category)
    
    async def get_by_id(self, category_id: int) -> Optional[Category]:
        """Récupère une catégorie par ID"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Category).where(Category.id == category_id)
            )
            return result.scalar_one_or_none()
    
    async def get_by_name(self, name: str) -> Optional[Category]:
        """Récupère une catégorie par nom"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Category).where(Category.name == name)
            )
            return result.scalar_one_or_none()
    
    async def get_with_children(self, category_id: int) -> Optional[Category]:
        """Récupère une catégorie avec ses sous-catégories"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Category)
                .options(selectinload(Category.subcategories))
                .where(Category.id == category_id)
            )
            return result.scalar_one_or_none()
    
    async def list_all(self) -> List[Category]:
        """Liste toutes les catégories"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Category).order_by(Category.name)
            )
            return result.scalars().all()
    
    async def list_root_categories(self) -> List[Category]:
        """Liste les catégories racines (sans parent)"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Category)
                .where(Category.parent_id.is_(None))
                .order_by(Category.name)
            )
            return result.scalars().all()
    
    async def get_count(self) -> int:
        """Compte le nombre de catégories"""
        async with self.db.get_session() as session:
            result = await session.execute(select(func.count(Category.id)))
            return result.scalar()
    
    async def create(self, category_data: dict) -> Category:
        """Crée une catégorie"""
        async with self.db.get_session() as session:
            category = Category(**category_data)
            session.add(category)
            await session.commit()
            await session.refresh(category)
            return category
    
    async def update(self, category_id: int, category_data: dict) -> Optional[Category]:
        """Met à jour une catégorie"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Category).where(Category.id == category_id)
            )
            category = result.scalar_one_or_none()
            
            if not category:
                return None
            
            for key, value in category_data.items():
                setattr(category, key, value)
            
            await session.commit()
            await session.refresh(category)
            return category
    
    async def delete(self, category_id: int) -> bool:
        """Supprime une catégorie"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Category).where(Category.id == category_id)
            )
            category = result.scalar_one_or_none()
            
            if not category:
                return False
            
            await session.delete(category)
            await session.commit()
            return True