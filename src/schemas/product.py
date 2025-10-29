from typing import Optional, List
from pydantic import BaseModel, Field, computed_field, field_validator
from datetime import datetime, timezone

from src.schemas.attribute import AttributeOut
from src.schemas.brand import BrandOut
from src.schemas.category import CategoryOut


class ProductImageSchema(BaseModel):
    url: str
    is_primary: bool = False

    class Config:
        from_attributes = True


class ProductAttributeValue(BaseModel):
    """Attribut avec sa valeur pour un produit"""

    attribute_id: int
    value: str = Field(..., max_length=255)


class ProductBase(BaseModel):
    description: Optional[str] = Field(None, max_length=2000)
    price: float = Field(..., gt=0)
    model: str = Field(..., max_length=100)
    condition: Optional[int] = Field(
        None, ge=0, le=10, description="null = neuf, 0-10 = occasion"
    )
    stock_quantity: int = Field(default=0, ge=0)
    is_featured: Optional[bool] = None
    is_daily_promo: Optional[bool] = None
    promo_percentage: Optional[int] = Field(
        None, ge=0, le=99, description="Pourcentage de réduction (0-99%)"
    )
    promo_start_date: Optional[datetime] = None
    promo_end_date: Optional[datetime] = None


class ProductCreate(ProductBase):
    image_urls: List[str] = Field(
        default_factory=list, description="URLs des images depuis CDN"
    )
    brand_id: int
    category_id: int
    attributes: List[ProductAttributeValue] = Field(
        default_factory=list, description="Attributs avec leurs valeurs"
    )


class ProductUpdate(BaseModel):
    description: Optional[str] = Field(None, max_length=2000)
    model: str = Field(..., max_length=100)
    price: Optional[float] = Field(None, gt=0)
    condition: Optional[int] = Field(None, ge=0, le=10)
    stock_quantity: Optional[int] = Field(None, ge=0)
    brand_id: Optional[int] = None
    category_id: Optional[int] = None
    image_urls: Optional[List[str]] = None
    attributes: Optional[List[ProductAttributeValue]] = None
    is_featured: Optional[bool] = None
    is_daily_promo: Optional[bool] = None
    promo_percentage: Optional[int] = Field(
        None, ge=0, le=99, description="Pourcentage de réduction (0-99%)"
    )
    promo_start_date: Optional[datetime] = None
    promo_end_date: Optional[datetime] = None


class PromoUpdate(BaseModel):
    """Mise à jour d'une promotion"""

    is_daily_promo: bool
    promo_percentage: Optional[int] = Field(
        None, ge=0, le=99, description="Pourcentage de réduction (0-99%)"
    )
    promo_start_date: Optional[datetime] = None
    promo_end_date: Optional[datetime] = None

    @field_validator("promo_end_date")
    def validate_end_date(cls, v, info):
        if (
            v
            and info.data.get("promo_start_date")
            and v <= info.data["promo_start_date"]
        ):
            raise ValueError("La date de fin doit être après la date de début")
        return v


# class ProductUpdate(BaseModel):
#     description: Optional[str] = Field(None, max_length=2000)
#     model: str = Field(..., max_length=100)
#     price: Optional[float] = Field(None, gt=0)
#     condition: Optional[int] = Field(None, ge=0, le=10)
#     stock_quantity: Optional[int] = Field(None, ge=0)
#     brand_id: Optional[int] = None
#     category_id: Optional[int] = None
#     image_urls: Optional[List[str]] = None
#     attributes: Optional[List[ProductAttributeValue]] = None


class ProductOut(BaseModel):
    id: str
    name: str
    description: Optional[str]
    price: float
    condition: Optional[int]
    stock_quantity: int
    is_featured: bool
    is_daily_promo: bool
    promo_percentage: Optional[int]
    promo_start_date: Optional[datetime]
    promo_end_date: Optional[datetime]
    created_at: datetime
    updated_at: Optional[datetime]
    images: List[ProductImageSchema] = []
    brand: Optional[BrandOut] = None
    category: Optional[CategoryOut] = None
    attributes: List[AttributeOut] = []

    @computed_field
    @property
    def discounted_price(self) -> Optional[float]:
        """Prix après réduction si promo active"""
        if self.is_daily_promo and self.promo_percentage:
            now = datetime.now(timezone.utc)
            if self.promo_start_date and self.promo_end_date:
                if self.promo_start_date <= now <= self.promo_end_date:
                    reduction = self.price * (self.promo_percentage / 100)
                    return round(self.price - reduction, 2)
        return None

    @computed_field
    @property
    def final_price(self) -> float:
        """Prix final (avec promo si active, sinon prix normal)"""
        return self.discounted_price if self.discounted_price else self.price

    class Config:
        from_attributes = True


class ProductListOut(BaseModel):
    products: List[ProductOut]
    total: int
    page: int
    page_size: int
    has_more: bool = False
