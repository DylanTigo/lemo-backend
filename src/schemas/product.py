from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime

from src.schemas.attribute import AttributeOut
from src.schemas.brand import BrandOut
from src.schemas.category import CategoryOut

class ProductImageSchema(BaseModel):
    url: str
    is_primary: int = 0  # 0 = False, 1 = True
    
    class Config:
        from_attributes = True

class ProductAttributeValue(BaseModel):
    """Attribut avec sa valeur pour un produit"""
    attribute_id: int
    value: str = Field(..., max_length=255)

class ProductBase(BaseModel):
    description: Optional[str] = Field(None, max_length=2000)
    price: float = Field(..., gt=0)
    condition: Optional[int] = Field(None, ge=0, le=10, description="null = neuf, 0-10 = occasion")
    stock_quantity: int = Field(default=0, ge=0)

class ProductCreate(ProductBase):
    id: Optional[str] = Field(None, description="SKU du produit")
    image_urls: List[str] = Field(default_factory=list, description="URLs des images depuis CDN")
    brand_id: int
    category_id: int
    attributes: List[ProductAttributeValue] = Field(default_factory=list, description="Attributs avec leurs valeurs")

class ProductUpdate(BaseModel):
    description: Optional[str] = Field(None, max_length=2000)
    price: Optional[float] = Field(None, gt=0)
    condition: Optional[int] = Field(None, ge=0, le=10)
    stock_quantity: Optional[int] = Field(None, ge=0)
    brand_id: Optional[int] = None
    category_id: Optional[int] = None
    image_urls: Optional[List[str]] = None
    attributes: Optional[List[ProductAttributeValue]] = None

class ProductOut(BaseModel):
    id: str
    name: str = Field(..., description="Nom générique auto-généré")
    description: Optional[str]
    price: float
    condition: Optional[int]
    stock_quantity: int
    created_at: datetime
    updated_at: Optional[datetime]
    images: List[ProductImageSchema] = []
    brand: Optional[BrandOut] = None
    category: Optional[CategoryOut] = None
    attributes: List[AttributeOut] = []
    
    class Config:
        from_attributes = True

class ProductListOut(BaseModel):
    products: List[ProductOut]
    total: int
    page: int
    page_size: int