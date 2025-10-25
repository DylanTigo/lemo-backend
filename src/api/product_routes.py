from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from src.schemas.product import ProductCreate, ProductUpdate, ProductOut
from src.services.product_services import ProductService
from src.repositories.product_repo import ProductRepository
from src.database import get_db, Database

router = APIRouter()

def get_product_service(db: Database = Depends(get_db)) -> ProductService:
    repo = ProductRepository(db)
    return ProductService(repo)

@router.get("/", response_model=List[ProductOut])
async def list_products(service: ProductService = Depends(get_product_service)):
    return await service.list_products()

@router.get("/{product_id}", response_model=ProductOut)
async def get_product(product_id: str, service: ProductService = Depends(get_product_service)):
    product = await service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

@router.post("/", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
async def create_product(payload: ProductCreate, service: ProductService = Depends(get_product_service)):
    product = await service.create_product(payload.model_dump(exclude_unset=True))
    return product

@router.put("/{product_id}", response_model=ProductOut)
async def update_product(product_id: str, payload: ProductUpdate, service: ProductService = Depends(get_product_service)):
    # ensure product exists
    existing = await service.get_product_by_id(product_id)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    updated = await service.update_product(product_id, payload.model_dump(exclude_unset=True))
    return updated

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: str, service: ProductService = Depends(get_product_service)):
    existing = await service.get_product_by_id(product_id)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    await service.delete_product(product_id)
    return None