from datetime import date

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


@router.get("/customers/{customer_id}")
def get_customer(
    customer_id: int,
    customer_service: CustomerService = Depends(get_customer_service),
):
    return customer_service.get_customer(customer_id)


@router.post("/customers")
def create_customer(
    name: str,
    email: str,
    date_of_birth: date,
    customer_service: CustomerService = Depends(get_customer_service),
):
    return customer_service.create_customer(
        name=name,
        email=email,
        date_of_birth=date_of_birth,
    )


@router.put("/customers/{customer_id}")
def update_customer(
    customer_id: int,
    name: str,
    email: str,
    date_of_birth: date,
    customer_service: CustomerService = Depends(get_customer_service),
):
    return customer_service.update_customer(
        customer_id=customer_id,
        name=name,
        email=email,
        date_of_birth=date_of_birth,
    )


@router.delete("/customers/{customer_id}")
def delete_customer(
    customer_id: int,
    customer_service: CustomerService = Depends(get_customer_service),
):
    return customer_service.delete_customer(customer_id)