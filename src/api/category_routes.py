from fastapi import APIRouter, Depends, HTTPException, status, Query
from src.services.cathegory_service import CategoryService, get_category_service
from src.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
    CategoryOut,
    CategoryWithChildren,
    CategoryListOut,
)
from src.middleware.auth_middleware import get_current_admin
from src.utils.exceptions import (
    NotFoundException,
    BadRequestException,
    LemoServiceException,
)
from src.utils.logging_config import logger


router = APIRouter(prefix="/categories", tags=["Categories"])

# Routes publiques


@router.get("", response_model=CategoryListOut)
async def list_categories(
    root_only: bool = Query(
        False, description="Afficher uniquement les catégories racines"
    ),
    category_service: CategoryService = Depends(get_category_service),
):
    """Liste les catégories (Public)"""
    try:
        return await category_service.list_categories(root_only=root_only)
    except LemoServiceException as e:
        logger.error(f"Failed to list categories: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/{category_id}", response_model=CategoryOut)
async def get_category(
    category_id: int, category_service: CategoryService = Depends(get_category_service)
):
    """Récupère une catégorie (Public)"""
    try:
        return await category_service.get_category(category_id)
    except LemoServiceException as e:
        logger.error(f"Failed to get category: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.get("/{category_id}/with-children", response_model=CategoryWithChildren)
async def get_category_with_children(
    category_id: int, category_service: CategoryService = Depends(get_category_service)
):
    """Récupère une catégorie avec ses sous-catégories (Public)"""
    try:
        return await category_service.get_category_with_children(category_id)
    except LemoServiceException as e:
        logger.error(f"Failed to get category with children: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


# Routes admin


@router.post("", response_model=CategoryOut, status_code=status.HTTP_201_CREATED)
async def create_category(
    category: CategoryCreate,
    category_service: CategoryService = Depends(get_category_service),
    # _current_admin = Depends(get_current_admin)
):
    """Crée une catégorie (Admin)"""
    try:
        return await category_service.create_category(category)
    except LemoServiceException as e:
        logger.error(f"Failed to create category: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.put("/{category_id}", response_model=CategoryOut)
async def update_category(
    category_id: int,
    category: CategoryUpdate,
    category_service: CategoryService = Depends(get_category_service),
    # _current_admin = Depends(get_current_admin)
):
    """Met à jour une catégorie (Admin)"""
    try:
        return await category_service.update_category(category_id, category)
    except LemoServiceException as e:
        logger.error(f"Failed to update category: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))


@router.delete("/{category_id}")
async def delete_category(
    category_id: int,
    category_service: CategoryService = Depends(get_category_service),
    # _current_admin = Depends(get_current_admin)
):
    """Supprime une catégorie (Admin)"""
    try:
        return await category_service.delete_category(category_id)
    except LemoServiceException as e:
        logger.error(f"Failed to delete category: {e}")
        raise HTTPException(status_code=e.status_code, detail=str(e))
