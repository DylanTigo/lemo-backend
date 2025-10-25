from typing import Optional, List
from fastapi import Depends
from src.repositories.product_repo import ProductRepository
from src.database import Database, get_db
from src.schemas.product import ProductCreate, ProductUpdate, ProductOut, ProductListOut
from src.utils.exceptions import NotFoundException
from src.models.product_images import ProductImage

class ProductService:
    def __init__(self, db: Database):
        self.db = db
        self.repo = ProductRepository(db)
    
    async def get_product(self, product_id: str) -> ProductOut:
        """Récupère un produit par ID"""
        product = await self.repo.get_by_id(product_id)
        if not product:
            raise NotFoundException(f"Produit {product_id} non trouvé")
        return ProductOut.model_validate(product)
    
    async def list_products(
        self,
        page: int = 1,
        page_size: int = 20,
        search: Optional[str] = None,
        category_id: Optional[int] = None,
        brand_id: Optional[int] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        condition: Optional[int] = None,
        is_new: Optional[bool] = None
    ) -> ProductListOut:
        """Liste les produits avec filtres"""
        skip = (page - 1) * page_size
        
        products, total = await self.repo.list_products(
            skip=skip,
            limit=page_size,
            search=search,
            category_id=category_id,
            brand_id=brand_id,
            min_price=min_price,
            max_price=max_price,
            condition=condition,
            is_new=is_new
        )
        
        products_out = [ProductOut.model_validate(p) for p in products]
        
        return ProductListOut(
            products=products_out,
            total=total,
            page=page,
            page_size=page_size
        )
    
    async def create_product(self, product_data: ProductCreate) -> ProductOut:
        """Crée un produit avec ses images (Admin)"""
        async with self.db.get_session() as session:
            # Extraire les URLs d'images
            image_urls = product_data.image_urls
            product_dict = product_data.model_dump(exclude={'image_urls'})
            
            # Créer le produit
            product = await self.repo.create_product(product_dict)
            
            # Ajouter les images si fournies
            if image_urls:
                for idx, url in enumerate(image_urls):
                    image = ProductImage(
                        product_id=product.id,
                        url=url,
                        is_primary=1 if idx == 0 else 0  # Première image = primaire
                    )
                    session.add(image)
                await session.commit()
            
            # Recharger le produit avec les images
            product = await self.repo.get_by_id(product.id)
            return ProductOut.model_validate(product)
    
    async def update_product(self, product_id: str, product_data: ProductUpdate) -> ProductOut:
        """Met à jour un produit (Admin)"""
        async with self.db.get_session() as session:
            update_data = product_data.model_dump(exclude_unset=True, exclude={'image_urls'})
            product = await self.repo.update_product(product_id, update_data)
            
            if not product:
                raise NotFoundException(f"Produit {product_id} non trouvé")
            
            # Mise à jour des images si fournies
            if product_data.image_urls is not None:
                # Supprimer les anciennes images
                for old_image in product.images:
                    await session.delete(old_image)
                
                # Ajouter les nouvelles
                for idx, url in enumerate(product_data.image_urls):
                    image = ProductImage(
                        product_id=product_id,
                        url=url,
                        is_primary=1 if idx == 0 else 0
                    )
                    session.add(image)
                
                await session.commit()
            
            # Recharger le produit
            product = await self.repo.get_by_id(product_id)
            return ProductOut.model_validate(product)
    
    async def delete_product(self, product_id: str) -> dict:
        """Supprime un produit (Admin)"""
        deleted = await self.repo.delete_product(product_id)
        
        if not deleted:
            raise NotFoundException(f"Produit {product_id} non trouvé")
        
        return {"message": f"Produit {product_id} supprimé avec succès"}


def get_product_service(db: Database = Depends(get_db)) -> ProductService:
    return ProductService(db)