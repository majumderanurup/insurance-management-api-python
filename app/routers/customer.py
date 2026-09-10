from fastapi import APIRouter, Depends

from app.dependencies import get_customer_service
from app.schemas.customer import CustomerRequest, CustomerResponse
from app.services.customer_service import CustomerService


router = APIRouter(
    tags=["Customer"]
)


@router.get("/customers", response_model=list[CustomerResponse])
def get_customers(
    customer_service: CustomerService = Depends(get_customer_service),
):
    return customer_service.get_customers()


@router.get("/customers/{customer_id}", response_model=CustomerResponse)
def get_customer(
    customer_id: int,
    customer_service: CustomerService = Depends(get_customer_service),
):
    return customer_service.get_customer(customer_id)


@router.post("/customers", response_model=CustomerResponse)
def create_customer(
    customer: CustomerRequest,
    customer_service: CustomerService = Depends(get_customer_service),
):
    return customer_service.create_customer(
        name=customer.name,
        email=customer.email,
        date_of_birth=customer.date_of_birth,
    )


@router.put("/customers/{customer_id}", response_model=CustomerResponse)
def update_customer(
    customer_id: int,
    customer: CustomerRequest,
    customer_service: CustomerService = Depends(get_customer_service),
):
    return customer_service.update_customer(
        customer_id=customer_id,
        name=customer.name,
        email=customer.email,
        date_of_birth=customer.date_of_birth,
    )


@router.delete("/customers/{customer_id}")
def delete_customer(
    customer_id: int,
    customer_service: CustomerService = Depends(get_customer_service),
):
    return customer_service.delete_customer(customer_id)