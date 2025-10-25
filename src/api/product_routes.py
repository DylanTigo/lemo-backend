from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from src.schemas.product import ProductCreate, ProductUpdate, ProductOut, ProductListOut
from src.services.product_services import get_product_service, ProductService
from src.database import get_db, Database

router = APIRouter()


@router.get("/", response_model=ProductListOut)
async def list_products(
    page: int = 1,
    page_size: int = 20,
    search: Optional[str] = None,
    category_id: Optional[int] = None,
    brand_id: Optional[int] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    condition: Optional[int] = None,
    is_new: Optional[bool] = None,
    service: ProductService = Depends(get_product_service),
):
    return await service.list_products(
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


@router.get("/{product_id}", response_model=ProductOut)
async def get_product(
    product_id: str, service: ProductService = Depends(get_product_service)
):
    return await service.get_product(product_id)


@router.post("/", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
async def create_product(
    payload: ProductCreate, service: ProductService = Depends(get_product_service)
):
    return await service.create_product(payload)


@router.put("/{product_id}", response_model=ProductOut)
async def update_product(
    product_id: str,
    payload: ProductUpdate,
    service: ProductService = Depends(get_product_service),
):
    return await service.update_product(product_id, payload)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: str, service: ProductService = Depends(get_product_service)
):
    return await service.delete_product(product_id)
