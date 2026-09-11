from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.customer_repository import CustomerRepository
from app.services.customer_service import CustomerService
from app.repositories.product_repository import ProductRepository
from app.services.product_service import ProductService


def get_customer_repository(
    db: Session = Depends(get_db),
) -> CustomerRepository:
    return CustomerRepository(db)


def get_customer_service(
    repository: CustomerRepository = Depends(get_customer_repository),
    db: Session = Depends(get_db),
) -> CustomerService:
    return CustomerService(repository, db)

def get_product_repository(
    db: Session = Depends(get_db),
) -> ProductRepository:
    return ProductRepository(db)


def get_product_service(
    repository: ProductRepository = Depends(get_product_repository),
    db: Session = Depends(get_db),
) -> ProductService:
    return ProductService(repository, db)