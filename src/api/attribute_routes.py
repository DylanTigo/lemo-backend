from fastapi import APIRouter, Depends, HTTPException, status
from src.services.attribute_service import AttributeService, get_attribute_service
from src.schemas.attribute import (
    AttributeCreate,
    AttributeUpdate,
    AttributeOut,
    AttributeListOut,
)
from src.middleware.auth_middleware import get_current_admin
from src.utils.exceptions import LemoServiceException
from src.utils.logging_config import logger

router = APIRouter(prefix="/attributes", tags=["Attributes"])

# Routes publiques


@router.get("", response_model=AttributeListOut)
async def list_attributes(
    attribute_service: AttributeService = Depends(get_attribute_service),
):
    """Liste les attributs (Public)"""
    try:
        return await attribute_service.list_attributes()
    except LemoServiceException as e:
        logger.error(f"Failed to list attributes: {e}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/{attribute_id}", response_model=AttributeOut)
async def get_attribute(
    attribute_id: int,
    attribute_service: AttributeService = Depends(get_attribute_service),
):
    """Récupère un attribut (Public)"""
    try:
        return await attribute_service.get_attribute(attribute_id)
    except LemoServiceException as e:
        logger.error(f"Failed to get attribute: {e}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


# Routes admin


@router.post("", response_model=AttributeOut, status_code=status.HTTP_201_CREATED)
async def create_attribute(
    attribute: AttributeCreate,
    attribute_service: AttributeService = Depends(get_attribute_service),
    _current_admin=Depends(get_current_admin),
):
    """Crée un attribut (Admin)"""
    try:
        return await attribute_service.create_attribute(attribute)
    except LemoServiceException as e:
        logger.error(f"Failed to create attribute: {e}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put("/{attribute_id}", response_model=AttributeOut)
async def update_attribute(
    attribute_id: int,
    attribute: AttributeUpdate,
    attribute_service: AttributeService = Depends(get_attribute_service),
    _current_admin=Depends(get_current_admin),
):
    """Met à jour un attribut (Admin)"""
    try:
        return await attribute_service.update_attribute(attribute_id, attribute)
    except LemoServiceException as e:
        logger.error(f"Failed to update attribute: {e}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{attribute_id}")
async def delete_attribute(
    attribute_id: int,
    attribute_service: AttributeService = Depends(get_attribute_service),
    _current_admin=Depends(get_current_admin),
):
    """Supprime un attribut (Admin)"""
    try:
        return await attribute_service.delete_attribute(attribute_id)
    except LemoServiceException as e:
        logger.error(f"Failed to delete attribute: {e}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
