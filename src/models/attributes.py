from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLEnum, func, Table
from sqlalchemy.orm import relationship

from src.database import Base
from src.models.associations import product_attributes
from src.schemas.enum import AttributeType

class Attribute(Base):
    __tablename__ = 'attributes'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(SQLEnum(AttributeType), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relations
    products = relationship("Product", secondary=product_attributes, back_populates="attributes")
    
    def __repr__(self):
        return f"<Attribute(id={self.id}, name='{self.name}', type='{self.type}')>"