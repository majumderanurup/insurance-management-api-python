from datetime import date

from app.models.customer import Customer
from app.repositories.customer_repository import CustomerRepository


class CustomerService:

    def __init__(
        self,
        repository: CustomerRepository,
        db,
    ):
        self.repository = repository
        self.db = db

    def get_customers(self):
        return self.repository.get_all()

    def get_customer(self, customer_id: int):
        return self.repository.get_by_id(customer_id)

    def create_customer(
        self,
        name: str,
        email: str,
        date_of_birth: date,
    ) -> Customer:
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
    ) -> Customer | None:
        customer = self.repository.get_by_id(customer_id)

        if customer is None:
            return None

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
            return False

        try:
            self.repository.delete(customer)
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            raise