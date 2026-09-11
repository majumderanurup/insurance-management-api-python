from fastapi import APIRouter, Depends

from app.dependencies import get_product_service
from app.schemas.product import ProductRequest, ProductResponse
from app.services.product_service import ProductService


router = APIRouter(
    tags=["Product"]
)


@router.get(
    "/products",
    response_model=list[ProductResponse],
)
def get_products(
    product_service: ProductService = Depends(get_product_service),
):
    return product_service.get_products()


@router.get(
    "/products/{product_id}",
    response_model=ProductResponse,
)
def get_product(
    product_id: int,
    product_service: ProductService = Depends(get_product_service),
):
    return product_service.get_product(product_id)


@router.post(
    "/products",
    response_model=ProductResponse,
)
def create_product(
    product: ProductRequest,
    product_service: ProductService = Depends(get_product_service),
):
    return product_service.create_product(
        name=product.name,
        description=product.description,
        product_type=product.type,
        min_entry_age=product.min_entry_age,
        max_entry_age=product.max_entry_age,
        min_sum_assured=product.min_sum_assured,
        max_sum_assured=product.max_sum_assured,
        active=product.active,
    )


@router.put(
    "/products/{product_id}",
    response_model=ProductResponse,
)
def update_product(
    product_id: int,
    product: ProductRequest,
    product_service: ProductService = Depends(get_product_service),
):
    return product_service.update_product(
        product_id=product_id,
        name=product.name,
        description=product.description,
        product_type=product.type,
        min_entry_age=product.min_entry_age,
        max_entry_age=product.max_entry_age,
        min_sum_assured=product.min_sum_assured,
        max_sum_assured=product.max_sum_assured,
        active=product.active,
    )


@router.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    product_service: ProductService = Depends(get_product_service),
):
    return product_service.delete_product(product_id)