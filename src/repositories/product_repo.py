from typing import Optional, List
from sqlalchemy import select, func, or_
from sqlalchemy.orm import selectinload
from src.models.products import Product
from src.repositories.base import BaseRepository
from src.database import Database


class ProductRepository(BaseRepository):
    def __init__(self, db: Database):
        super().__init__(db, Product)

    async def get_by_id(self, product_id: str) -> Optional[Product]:
        """Récupère un produit par ID avec ses images"""
        async with self.db.get_session() as session:
            query = (
                select(Product)
                .options(selectinload(Product.images))
                .where(Product.id == product_id)
            )
            result = await session.execute(query)
            return result.scalar_one_or_none()

    async def list_products(
        self,
        skip: int = 0,
        limit: int = 20,
        search: Optional[str] = None,
        category_id: Optional[int] = None,
        brand_id: Optional[int] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        condition: Optional[int] = None,
        is_new: Optional[bool] = None,
    ) -> tuple[List[Product], int]:
        """Liste les produits avec filtres et pagination"""
        async with self.db.get_session() as session:
            query = select(Product).options(selectinload(Product.images))

            # Filtre recherche textuelle (sur le nom générique indexé)
            if search:
                query = query.where(Product.name.ilike(f"%{search}%"))

            # Filtres
            if category_id:
                query = query.where(Product.category_id == category_id)

            if brand_id:
                query = query.where(Product.brand_id == brand_id)

            if min_price is not None:
                query = query.where(Product.price >= min_price)

            if max_price is not None:
                query = query.where(Product.price <= max_price)

            if is_new is not None:
                if is_new:
                    query = query.where(Product.condition.is_(None))
                else:
                    query = query.where(Product.condition.isnot(None))
            elif condition is not None:
                query = query.where(Product.condition == condition)

            # Compte total
            count_query = select(func.count()).select_from(query.subquery())
            total = await session.scalar(count_query)

            # Pagination
            query = query.offset(skip).limit(limit).order_by(Product.created_at.desc())

            result = await session.execute(query)
            products = result.scalars().all()

            return products, total

    async def create_product(self, product_data: dict) -> Product:
        """Crée un produit"""
        async with self.db.get_session() as session:
            product = Product(**product_data)
            session.add(product)
            await session.commit()
            await session.refresh(product)
            return product

    async def update_product(
        self, product_id: str, product_data: dict
    ) -> Optional[Product]:
        """Met à jour un produit"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Product).where(Product.id == product_id)
            )
            product = result.scalar_one_or_none()

            if not product:
                return None

            for key, value in product_data.items():
                if value is not None:
                    setattr(product, key, value)

            await session.commit()
            await session.refresh(product)
            return product

    async def delete_product(self, product_id: str) -> bool:
        """Supprime un produit"""
        async with self.db.get_session() as session:
            result = await session.execute(
                select(Product).where(Product.id == product_id)
            )
            product = result.scalar_one_or_none()

            if not product:
                return False

            await session.delete(product)
            await session.commit()
            return True
