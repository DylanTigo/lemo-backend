from typing import Optional, List
from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime

class ProductImageSchema(BaseModel):
    url: str
    is_primary: int = 0  # 0 = False, 1 = True
    
    class Config:
        from_attributes = True

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200, description="Nom générique: Catégorie + Marque + Model + Attributs")
    description: Optional[str] = Field(None, max_length=2000)
    price: float = Field(..., gt=0)
    condition: Optional[int] = Field(None, ge=0, le=10, description="null = neuf, 0-10 = occasion")
    stock_quantity: int = Field(default=0, ge=0)
    brand_id: Optional[int] = None
    category_id: Optional[int] = None

class ProductCreate(ProductBase):
    id: str  # ID personnalisé (SKU)
    image_urls: List[str] = Field(default_factory=list, description="URLs des images depuis CDN")

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=2000)
    price: Optional[float] = Field(None, gt=0)
    condition: Optional[int] = Field(None, ge=0, le=10)
    stock_quantity: Optional[int] = Field(None, ge=0)
    brand_id: Optional[int] = None
    category_id: Optional[int] = None
    image_urls: Optional[List[str]] = None

class ProductOut(ProductBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime]
    images: List[ProductImageSchema] = []
    
    class Config:
        from_attributes = True

class ProductListOut(BaseModel):
    products: List[ProductOut]
    total: int
    page: int
    page_size: int