from sqlalchemy import Float, Table, Column, Integer, ForeignKey, String
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

# Table de liaison pour product_attributes
product_attributes = Table(
    "product_attributes",
    Base.metadata,
    Column(
        "product_id",
        String(255),
        ForeignKey("products.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "attribute_id",
        Integer,
        ForeignKey("attributes.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column("value", String(255), nullable=False),
)
