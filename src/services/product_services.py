from fastapi import Depends
from typing import Optional
from src.models.products import Product
from src.repositories.product_repo import ProductRepository
import uuid


class ProductService:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    async def get_product_by_id(self, product_id: str) -> Optional[Product]:
        return await self.product_repo.get_by_id(product_id)

    async def create_product(self, product_data) -> Product:
        # Ensure ID exists since Product.id is a non-nullable String PK
        if not product_data.get("id"):
            product_data["id"] = str(uuid.uuid4())
        return await self.product_repo.create(product_data)

    async def list_products(self) -> list[Product]:
        return await self.product_repo.list_all()

    async def update_product(self, product_id: str, product_data) -> Product:
        return await self.product_repo.update(product_id, product_data)

    async def delete_product(self, product_id: str):
        return await self.product_repo.delete(product_id)
