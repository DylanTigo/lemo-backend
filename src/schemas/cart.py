from typing import List
from pydantic import BaseModel, Field
from src.schemas.product import ProductOut

class CartRequest(BaseModel):
    """Requête pour récupérer les produits du panier"""
    product_ids: List[str] = Field(..., min_length=1, description="Liste des IDs produits du panier")

class CartProductOut(BaseModel):
    """Produit avec disponibilité"""
    product: ProductOut
    is_available: bool = Field(..., description="Produit en stock")
    stock_quantity: int = Field(..., description="Quantité disponible")

class CartResponse(BaseModel):
    """Réponse avec les produits du panier"""
    products: List[CartProductOut]
    total_products: int
    unavailable_count: int = Field(..., description="Nombre de produits indisponibles")