from sqlalchemy import TIMESTAMP, Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from src.database import Base

class Brand(Base):
    __tablename__ = 'brands'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(500))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())

    # Relations
    products = relationship("Product", back_populates="brand")
    
    def __repr__(self):
        return f"<Brand(id={self.id}, name='{self.name}')>"