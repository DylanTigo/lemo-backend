
from uuid import uuid4
from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey, func, Table, Enum as SQLEnum
from sqlalchemy.orm import relationship

from src.database import Base
from src.models.associations import order_products, product_attributes

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid4()))
    brand_id = Column(Integer, ForeignKey('brands.id', ondelete='SET NULL'), nullable=True)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='SET NULL'), nullable=True)
    name = Column(String, nullable=False, index=True, unique=True)
    description = Column(String(2000))
    price = Column(Float, nullable=False)
    condition = Column(Integer, nullable=True, default=0)
    model = Column(String(100), nullable=True)
    stock_quantity = Column(Integer, nullable=False, default=0)
    state = Column(SQLEnum("new", "used", name="product_state"), nullable=False, default="new")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    is_featured = Column(Boolean, default=False, index=True)  # Produit en vedette
    is_daily_promo = Column(Boolean, default=False, index=True)  # Promo du jour
    promo_percentage = Column(Integer, nullable=True)  # Pourcentage de réduction (ex: 15 = 15%)
    promo_start_date = Column(DateTime(timezone=True), nullable=True)  # Début promo
    promo_end_date = Column(DateTime(timezone=True), nullable=True)  # Fin promo
    
    # Relations
    brand = relationship("Brand", back_populates="products")
    category = relationship("Category", back_populates="products")
    images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")
    attributes = relationship("Attribute", secondary=product_attributes, back_populates="products")
    orders = relationship("Order", secondary=order_products, back_populates="products")
    
    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"