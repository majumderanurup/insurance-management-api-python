from fastapi import APIRouter

from app.services.customer_service import CustomerService

router = APIRouter(
    tags=["Customer"]
)

customer_service = CustomerService()


@router.get("/customers")
def get_customers():
    return customer_service.get_customers()