from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime


class CategoryBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    parent_id: Optional[int] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    parent_id: Optional[int] = None


class CategoryOut(CategoryBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class CategoryWithChildren(CategoryOut):
    subcategories: List["CategoryOut"] = []


class CategoryListOut(BaseModel):
    categories: List[CategoryOut]
    total: int
