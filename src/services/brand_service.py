from typing import List
from fastapi import Depends
from src.repositories.brand_repo import BrandRepository
from src.database import Database, get_db
from src.schemas.brand import BrandCreate, BrandUpdate, BrandOut, BrandListOut
from src.utils.exceptions import NotFoundException

class BrandService:
    def __init__(self, db: Database):
        self.db = db
        self.repo = BrandRepository(db)
    
    async def get_brand(self, brand_id: int) -> BrandOut:
        """Récupère une marque"""
        brand = await self.repo.get_by_id(brand_id)
        if not brand:
            raise NotFoundException(f"Marque {brand_id} non trouvée")
        return BrandOut.model_validate(brand)
    
    async def list_brands(self) -> BrandListOut:
        """Liste les marques"""
        brands = await self.repo.list_all()
        total = await self.repo.get_count()
        brands_out = [BrandOut.model_validate(b) for b in brands]
        
        return BrandListOut(brands=brands_out, total=total)
    
    async def create_brand(self, brand_data: BrandCreate) -> BrandOut:
        """Crée une marque (Admin)"""
        # Vérifier si le nom existe déjà
        existing = await self.repo.get_by_name(brand_data.name)
        if existing:
            raise ValueError(f"La marque '{brand_data.name}' existe déjà")
        
        brand = await self.repo.create(brand_data.model_dump())
        return BrandOut.model_validate(brand)
    
    async def update_brand(self, brand_id: int, brand_data: BrandUpdate) -> BrandOut:
        """Met à jour une marque (Admin)"""
        update_data = brand_data.model_dump(exclude_unset=True)
        
        # Vérifier si le nouveau nom existe déjà
        if 'name' in update_data:
            existing = await self.repo.get_by_name(update_data['name'])
            if existing and existing.id != brand_id:
                raise ValueError(f"La marque '{update_data['name']}' existe déjà")
        
        brand = await self.repo.update(brand_id, update_data)
        if not brand:
            raise NotFoundException(f"Marque {brand_id} non trouvée")
        
        return BrandOut.model_validate(brand)
    
    async def delete_brand(self, brand_id: int) -> dict:
        """Supprime une marque (Admin)"""
        deleted = await self.repo.delete(brand_id)
        if not deleted:
            raise NotFoundException(f"Marque {brand_id} non trouvée")
        
        return {"message": f"Marque {brand_id} supprimée avec succès"}


def get_brand_service(db: Database = Depends(get_db)) -> BrandService:
    return BrandService(db)