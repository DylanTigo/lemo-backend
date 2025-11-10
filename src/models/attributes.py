from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLEnum, func, ARRAY
from sqlalchemy.orm import relationship

from src.database import Base
from src.schemas.enum import AttributeType

class Attribute(Base):
    __tablename__ = 'attributes'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    type = Column(SQLEnum(AttributeType), nullable=False)
    list_values = Column(ARRAY(String), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relations
    product_attributes = relationship("ProductAttribute", back_populates="attribute", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Attribute(id={self.id}, name='{self.name}', type='{self.type}')>"