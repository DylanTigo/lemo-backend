from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float, Enum as SQLEnum, Table, func
from sqlalchemy.orm import relationship

from src.database import Base
from src.models.associations import order_products
from src.schemas.enum import OrderStatus

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    order_date = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(SQLEnum(OrderStatus), default=OrderStatus.PENDING, nullable=False)
    total_amount = Column(Float, nullable=False, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relations
    user = relationship("User", back_populates="orders")
    products = relationship("Product", secondary=order_products, back_populates="orders")
    
    def __repr__(self):
        return f"<Order(id={self.id}, user_id={self.user_id}, status='{self.status}', total={self.total_amount})>"