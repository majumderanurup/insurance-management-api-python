import logging
from datetime import date

from sqlalchemy.orm import Session

from app.exceptions.customer import (
    CustomerAlreadyExistsException,
    CustomerNotFoundException,
)
from app.models.customer import Customer
from app.repositories.customer_repository import CustomerRepository


logger = logging.getLogger(__name__)


class CustomerService:

    def __init__(
        self,
        repository: CustomerRepository,
        db: Session,
    ):
        self.repository = repository
        self.db = db

    def get_customers(self):
        logger.info("Fetching all customers")
        return self.repository.get_all()

    def get_customer(self, customer_id: int):
        logger.info("Fetching customer with id: %s", customer_id)

        customer = self.repository.get_by_id(customer_id)

        if customer is None:
            logger.warning(
                "Customer not found: %s",
                customer_id,
            )
            raise CustomerNotFoundException(customer_id)

        return customer

    def create_customer(
        self,
        name: str,
        email: str,
        date_of_birth: date,
    ) -> Customer:

        logger.info("Creating customer with email: %s", email)

        existing_customer = self.repository.get_by_email(email)

        if existing_customer is not None:
            logger.warning(
                "Customer creation failed: email already exists: %s",
                email,
            )
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

            logger.info(
                "Customer created successfully with id: %s",
                customer.id,
            )

            return customer

        except Exception:
            self.db.rollback()
            logger.exception(
                "Failed to create customer with email: %s",
                email,
            )
            raise

    def update_customer(
        self,
        customer_id: int,
        name: str,
        email: str,
        date_of_birth: date,
    ) -> Customer:

        logger.info(
            "Updating customer with id: %s",
            customer_id,
        )

        customer = self.repository.get_by_id(customer_id)

        if customer is None:
            logger.warning(
                "Customer not found: %s",
                customer_id,
            )
            raise CustomerNotFoundException(customer_id)

        existing_customer = (
            self.repository.get_by_email_excluding_customer(
                email,
                customer_id,
            )
        )

        if existing_customer is not None:
            logger.warning(
                "Customer update failed: email already exists: %s",
                email,
            )
            raise CustomerAlreadyExistsException(email)

        customer.name = name
        customer.email = email
        customer.date_of_birth = date_of_birth

        try:
            self.repository.update(customer)
            self.db.commit()
            self.db.refresh(customer)

            logger.info(
                "Customer updated successfully with id: %s",
                customer_id,
            )

            return customer

        except Exception:
            self.db.rollback()
            logger.exception(
                "Failed to update customer with id: %s",
                customer_id,
            )
            raise

    def delete_customer(self, customer_id: int) -> bool:
        logger.info(
            "Deleting customer with id: %s",
            customer_id,
        )

        customer = self.repository.get_by_id(customer_id)

        if customer is None:
            logger.warning(
                "Customer not found: %s",
                customer_id,
            )
            raise CustomerNotFoundException(customer_id)

        try:
            self.repository.delete(customer)
            self.db.commit()

            logger.info(
                "Customer deleted successfully with id: %s",
                customer_id,
            )

            return True

        except Exception:
            self.db.rollback()
            logger.exception(
                "Failed to delete customer with id: %s",
                customer_id,
            )
            raise