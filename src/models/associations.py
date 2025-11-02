from sqlalchemy import Float, Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from src.database import Base

order_products = Table(
    "order_products",
    Base.metadata,
    Column(
        "order_id",
        Integer,
        ForeignKey("orders.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "product_id",
        String(255),
        ForeignKey("products.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column("quantity", Integer, nullable=False, default=1),
    Column("price_at_purchase", Float, nullable=False),
)

# Modèle d'association pour product_attributes avec accès à la valeur
class ProductAttribute(Base):
    __tablename__ = "product_attributes"
    
    product_id = Column(
        String(255),
        ForeignKey("products.id", ondelete="CASCADE"),
        primary_key=True,
    )
    attribute_id = Column(
        Integer,
        ForeignKey("attributes.id", ondelete="CASCADE"),
        primary_key=True,
    )
    value = Column(String(255), nullable=False)
    
    # Relations
    product = relationship("Product", back_populates="product_attributes")
    attribute = relationship("Attribute", back_populates="product_attributes")
    
    def __repr__(self):
        return f"<ProductAttribute(product_id={self.product_id}, attribute_id={self.attribute_id}, value='{self.value}')>"
