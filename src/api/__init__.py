from fastapi import APIRouter
from .product_routes import router as product_router
from .auth_routes import router as auth_router

api_router = APIRouter()

api_router.include_router(product_router, prefix="/products", tags=["products"])
api_router.include_router(auth_router, prefix="/auth", tags=["authentication"])
