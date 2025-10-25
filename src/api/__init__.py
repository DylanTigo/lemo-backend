from fastapi import APIRouter
from .product_routes import router as product_router
from .auth_routes import router as auth_router
from .category_routes import router as category_router
from .brand_routes import router as brand_router
from .attribute_routes import router as attribute_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(product_router)
api_router.include_router(category_router)
api_router.include_router(brand_router)
api_router.include_router(attribute_router)