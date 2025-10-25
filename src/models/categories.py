from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from src.database import Base

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    parent_id = Column(Integer, ForeignKey('categories.id', ondelete='SET NULL'), nullable=True)
    description = Column(String(500))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relations
    parent = relationship("Category", remote_side=[id], backref="subcategories")
    products = relationship("Product", back_populates="category")
    
    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"