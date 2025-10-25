from typing import Optional
from pydantic import EmailStr
from sqlalchemy.future import select
from src.repositories.main import BaseRepository
from src.database import Database
from src.models.products import Product


class ProductRepository(BaseRepository):
  def __init__(self, db: Database):
    super().__init__(db, Product)

  async def create(self, obj_data):
    return await super().create(obj_data)