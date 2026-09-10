from fastapi import APIRouter, Depends

from app.dependencies import get_customer_service
from app.services.customer_service import CustomerService

router = APIRouter(
    tags=["Customer"]
)


@router.get("/customers")
def get_customers(
    customer_service: CustomerService = Depends(get_customer_service),
):
    return customer_service.get_customers()