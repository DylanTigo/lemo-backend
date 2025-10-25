from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from src.schemas.enum import AttributeType

class AttributeBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    type: AttributeType

class AttributeCreate(AttributeBase):
    pass

class AttributeUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    type: Optional[AttributeType] = None

class AttributeOut(AttributeBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True

class AttributeListOut(BaseModel):
    attributes: list[AttributeOut]
    total: int