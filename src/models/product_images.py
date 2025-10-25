from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from src.database import Base

class ProductImage(Base):
    __tablename__ = 'product_images'
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String(255), ForeignKey('products.id', ondelete='CASCADE'), nullable=False)
    url = Column(String(500), nullable=False)
    is_primary = Column(Integer, default=0)  # 0 = False, 1 = True
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relations
    product = relationship("Product", back_populates="images")
    
    def __repr__(self):
        return f"<ProductImage(id={self.id}, product_id={self.product_id})>"