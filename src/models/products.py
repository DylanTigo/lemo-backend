
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func, Table, Enum as SQLEnum
from sqlalchemy.orm import relationship

from src.database import Base
from src.models.associations import order_products, product_attributes

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(String(255), primary_key=True, index=True)
    brand_id = Column(Integer, ForeignKey('brands.id', ondelete='SET NULL'), nullable=True)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='SET NULL'), nullable=True)
    name = Column(String(200), nullable=False, index=True)
    description = Column(String(2000))
    price = Column(Float, nullable=False)
    condition = Column(Integer, nullable=True, default=0)
    state = Column(SQLEnum("new", "used", name="product_state"), nullable=False, default="new")
    stock_quantity = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relations
    brand = relationship("Brand", back_populates="products")
    category = relationship("Category", back_populates="products")
    images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")
    attributes = relationship("Attribute", secondary=product_attributes, back_populates="products")
    orders = relationship("Order", secondary=order_products, back_populates="products")
    
    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"