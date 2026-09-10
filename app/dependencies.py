from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.customer_repository import CustomerRepository
from app.services.customer_service import CustomerService


def get_customer_repository(
    db: Session = Depends(get_db),
) -> CustomerRepository:
    return CustomerRepository(db)


def get_customer_service(
    repository: CustomerRepository = Depends(get_customer_repository),
    db: Session = Depends(get_db),
) -> CustomerService:
    return CustomerService(repository, db)