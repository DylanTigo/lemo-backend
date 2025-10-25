from fastapi import APIRouter, Depends, HTTPException, status
from src.services.brand_service import BrandService, get_brand_service
from src.schemas.brand import BrandCreate, BrandUpdate, BrandOut, BrandListOut
from src.middleware.auth_middleware import get_current_admin
from src.utils.exceptions import NotFoundException, BadRequestException

router = APIRouter(prefix="/brands", tags=["Brands"])

# Routes publiques

@router.get("", response_model=BrandListOut)
async def list_brands(
    brand_service: BrandService = Depends(get_brand_service)
):
    """Liste les marques (Public)"""
    return await brand_service.list_brands()

@router.get("/{brand_id}", response_model=BrandOut)
async def get_brand(
    brand_id: int,
    brand_service: BrandService = Depends(get_brand_service)
):
    """Récupère une marque (Public)"""
    try:
        return await brand_service.get_brand(brand_id)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

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
    except BadRequestException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

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
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except BadRequestException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{brand_id}")
async def delete_brand(
    brand_id: int,
    brand_service: BrandService = Depends(get_brand_service),
    # _current_admin = Depends(get_current_admin)
):
    """Supprime une marque (Admin)"""
    try:
        return await brand_service.delete_brand(brand_id)
    except NotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))