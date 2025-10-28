from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from src.services.product_service import ProductService, get_product_service
from src.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductOut,
    ProductListOut,
    PromoUpdate,
)
from src.middleware.auth_middleware import get_current_admin
from src.utils.exceptions import NotFoundException
from src.utils.logging_config import logger

router = APIRouter(prefix="/products", tags=["Products"])

# Routes publiques


@router.get("", response_model=ProductListOut)
async def list_products(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    search: Optional[str] = None,
    category_id: Optional[int] = None,
    brand_id: Optional[int] = None,
    min_price: Optional[float] = Query(None, ge=0),
    max_price: Optional[float] = Query(None, ge=0),
    condition: Optional[int] = Query(None, ge=0, le=10),
    is_new: Optional[bool] = None,
    product_service: ProductService = Depends(get_product_service),
    latest_products: Optional[bool] = Query(False),
    latest_products_count: Optional[int] = Query(6),
):
    """Liste tous les produits avec filtres (Public)"""
    try:
        return await product_service.list_products(
            page=page,
            page_size=page_size,
            search=search,
            category_id=category_id,
            brand_id=brand_id,
            min_price=min_price,
            max_price=max_price,
            condition=condition,
            is_new=is_new,
            latest_products=latest_products,
            latest_products_count=latest_products_count,
        )
    except Exception as e:
        logger.error(f"Error listing products: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de la récupération des produits",
        )


@router.get("/{product_id}", response_model=ProductOut)
async def get_product(
    product_id: str, product_service: ProductService = Depends(get_product_service)
):
    """Récupère un produit par ID (Public)"""
    try:
        return await product_service.get_product(product_id)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        logger.error(f"Error getting product {product_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de la récupération du produit",
        )


@router.get("/featured", response_model=List[ProductOut])
async def get_featured_products(
    limit: int = Query(10, ge=1, le=50, description="Nombre de produits à retourner"),
    product_service: ProductService = Depends(get_product_service),
):
    """Liste les produits en vedette (Public)"""
    try:
        return await product_service.list_featured_products(limit)
    except Exception as e:
        logger.error(f"Error getting featured products: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de la récupération des produits en vedette",
        )


@router.get("/daily-promo", response_model=List[ProductOut])
async def get_daily_promos(
    limit: int = Query(20, ge=1, le=50, description="Nombre de promotions à retourner"),
    product_service: ProductService = Depends(get_product_service),
):
    """Liste les promotions du jour actives (Public)"""
    try:
        return await product_service.list_daily_promos(limit)
    except Exception as e:
        logger.error(f"Error getting daily promos: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de la récupération des promotions",
        )


@router.get("", response_model=ProductListOut)
async def list_products(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    search: Optional[str] = None,
    category_id: Optional[int] = None,
    brand_id: Optional[int] = None,
    min_price: Optional[float] = Query(None, ge=0),
    max_price: Optional[float] = Query(None, ge=0),
    condition: Optional[int] = Query(None, ge=0, le=10),
    is_new: Optional[bool] = None,
    product_service: ProductService = Depends(get_product_service),
):
    """Liste tous les produits avec filtres (Public)"""
    try:
        return await product_service.list_products(
            page=page,
            page_size=page_size,
            search=search,
            category_id=category_id,
            brand_id=brand_id,
            min_price=min_price,
            max_price=max_price,
            condition=condition,
            is_new=is_new,
        )
    except Exception as e:
        logger.error(f"Error listing products: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de la récupération des produits",
        )


@router.get("/{product_id}", response_model=ProductOut)
async def get_product(
    product_id: str, product_service: ProductService = Depends(get_product_service)
):
    """Récupère un produit par ID (Public)"""
    try:
        return await product_service.get_product(product_id)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        logger.error(f"Error getting product {product_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de la récupération du produit",
        )


# Routes protégées (Admin uniquement)


@router.post("", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
async def create_product(
    product: ProductCreate,
    product_service: ProductService = Depends(get_product_service),
    _current_admin=Depends(get_current_admin),
):
    """Crée un produit (Admin)"""
    try:
        return await product_service.create_product(product)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Error creating product: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de la création: {str(e)}",
        )


@router.put("/{product_id}", response_model=ProductOut)
async def update_product(
    product_id: str,
    product: ProductUpdate,
    product_service: ProductService = Depends(get_product_service),
    _current_admin=Depends(get_current_admin),
):
    """Met à jour un produit (Admin)"""
    try:
        return await product_service.update_product(product_id, product)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Error updating product {product_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de la mise à jour",
        )


@router.patch("/{product_id}/promo", response_model=ProductOut)
async def update_product_promo(
    product_id: str,
    promo: PromoUpdate,
    product_service: ProductService = Depends(get_product_service),
    _current_admin=Depends(get_current_admin),
):
    """Met à jour la promotion d'un produit (Admin)"""
    try:
        return await product_service.update_product_promo(product_id, promo)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        logger.error(f"Error updating product {product_id} promo: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de la mise à jour de la promotion",
        )


@router.delete("/{product_id}")
async def delete_product(
    product_id: str,
    product_service: ProductService = Depends(get_product_service),
    _current_admin=Depends(get_current_admin),
):
    """Supprime un produit (Admin)"""
    try:
        return await product_service.delete_product(product_id)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except Exception as e:
        logger.error(f"Error deleting product {product_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de la suppression",
        )
