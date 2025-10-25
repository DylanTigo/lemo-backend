from pydantic import BaseModel, EmailStr
from datetime import datetime
from src.schemas.enum import UserRole

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole
    created_at: datetime
    
    class Config:
        from_attributes = True