from fastapi import APIRouter, Depends, HTTPException, status
from src.services.brand_service import BrandService, get_brand_service
from src.schemas.brand import BrandCreate, BrandUpdate, BrandOut, BrandListOut
from src.middleware.auth_middleware import get_current_admin
from src.utils.exceptions import LemoServiceException
from src.utils.logging_config import logger

router = APIRouter(prefix="/brands", tags=["Brands"])

# Routes publiques

@router.get("", response_model=BrandListOut)
async def list_brands(
    brand_service: BrandService = Depends(get_brand_service)
):
    """Liste les marques (Public)"""
    try:
        return await brand_service.list_brands()
    except LemoServiceException as e:
        logger.error(f"Failed to list brands: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))

@router.get("/{brand_id}", response_model=BrandOut)
async def get_brand(
    brand_id: int,
    brand_service: BrandService = Depends(get_brand_service)
):
    """Récupère une marque (Public)"""
    try:
        return await brand_service.get_brand(brand_id)
    except LemoServiceException as e:
        logger.error(f"Failed to get brand: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))

# Routes admin

@router.post("", response_model=BrandOut, status_code=status.HTTP_201_CREATED)
async def create_brand(
    brand: BrandCreate,
    brand_service: BrandService = Depends(get_brand_service),
    # _current_admin = Depends(get_current_admin)
):
    """Crée une marque (Admin)"""
    try:
        return await brand_service.create_brand(brand)
    except LemoServiceException as e:
        logger.error(f"Failed to create brand: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))

@router.put("/{brand_id}", response_model=BrandOut)
async def update_brand(
    brand_id: int,
    brand: BrandUpdate,
    brand_service: BrandService = Depends(get_brand_service),
    # _current_admin = Depends(get_current_admin)
):
    """Met à jour une marque (Admin)"""
    try:
        return await brand_service.update_brand(brand_id, brand)
    except LemoServiceException as e:
        logger.error(f"Failed to update brand: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))

@router.delete("/{brand_id}")
async def delete_brand(
    brand_id: int,
    brand_service: BrandService = Depends(get_brand_service),
    # _current_admin = Depends(get_current_admin)
):
    """Supprime une marque (Admin)"""
    try:
        return await brand_service.delete_brand(brand_id)
    except LemoServiceException as e:
        logger.error(f"Failed to delete brand: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))