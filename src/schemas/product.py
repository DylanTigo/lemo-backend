from typing import Optional, List
from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(..., max_length=200)
    description: Optional[str] = Field(None, max_length=2000)
    price: float
    condition: Optional[int] = 0
    state: Optional[str] = Field("new", pattern="^(new|used)$")
    stock_quantity: Optional[int] = 0
    brand_id: Optional[int] = None
    category_id: Optional[int] = None


class ProductCreate(ProductBase):
    id: Optional[str] = None


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = Field(None, max_length=2000)
    price: Optional[float] = None
    condition: Optional[int] = None
    state: Optional[str] = Field(None, pattern="^(new|used)$")
    stock_quantity: Optional[int] = None
    brand_id: Optional[int] = None
    category_id: Optional[int] = None


class ProductOut(ProductBase):
    id: str

    class Config:
        from_attributes = True
