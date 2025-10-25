# Ensure all models are imported so SQLAlchemy registers tables before create_all
from .brands import Brand  # noqa: F401
from .categories import Category  # noqa: F401
from .products import Product  # noqa: F401
from .product_images import ProductImage  # noqa: F401
from .attributes import Attribute  # noqa: F401
from .orders import Order  # noqa: F401
from .users import User  # noqa: F401
from .associations import order_products, product_attributes  # noqa: F401
