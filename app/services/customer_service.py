from datetime import date

from sqlalchemy.orm import Session

from app.exceptions.customer import (
    CustomerAlreadyExistsException,
    CustomerNotFoundException,
)
from app.models.customer import Customer
from app.repositories.customer_repository import CustomerRepository


class CustomerService:

    def __init__(
        self,
        repository: CustomerRepository,
        db: Session,
    ):
        self.repository = repository
        self.db = db

    def get_customers(self):
        return self.repository.get_all()

    def get_customer(self, customer_id: int):
        customer = self.repository.get_by_id(customer_id)

        if customer is None:
            raise CustomerNotFoundException(customer_id)

        return customer

    def create_customer(
        self,
        name: str,
        email: str,
        date_of_birth: date,
    ) -> Customer:

        existing_customer = self.repository.get_by_email(email)

        if existing_customer is not None:
            raise CustomerAlreadyExistsException(email)

        customer = Customer(
            name=name,
            email=email,
            date_of_birth=date_of_birth,
        )

        try:
            customer = self.repository.create(customer)
            self.db.commit()
            self.db.refresh(customer)
            return customer
        except Exception:
            self.db.rollback()
            raise

    def update_customer(
        self,
        customer_id: int,
        name: str,
        email: str,
        date_of_birth: date,
    ) -> Customer:

        customer = self.repository.get_by_id(customer_id)

        if customer is None:
            raise CustomerNotFoundException(customer_id)

        existing_customer = self.repository.get_by_email_excluding_customer(
            email,
            customer_id,
        )

        if existing_customer is not None:
            raise CustomerAlreadyExistsException(email)

        customer.name = name
        customer.email = email
        customer.date_of_birth = date_of_birth

        try:
            self.repository.update(customer)
            self.db.commit()
            self.db.refresh(customer)
            return customer
        except Exception:
            self.db.rollback()
            raise

    def delete_customer(self, customer_id: int) -> bool:
        customer = self.repository.get_by_id(customer_id)

        if customer is None:
            raise CustomerNotFoundException(customer_id)

        try:
            self.repository.delete(customer)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            raise