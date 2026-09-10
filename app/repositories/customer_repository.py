from sqlalchemy.orm import Session

from app.models.customer import Customer


class CustomerRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Customer]:
        return self.db.query(Customer).all()

    def get_by_id(self, customer_id: int) -> Customer | None:
        return (
            self.db.query(Customer)
            .filter(Customer.id == customer_id)
            .first()
        )

    def get_by_email(self, email: str) -> Customer | None:
        return (
            self.db.query(Customer)
            .filter(Customer.email == email)
            .first()
        )

    def get_by_email_excluding_customer(
        self,
        email: str,
        customer_id: int,
    ) -> Customer | None:
        return (
            self.db.query(Customer)
            .filter(
                Customer.email == email,
                Customer.id != customer_id,
            )
            .first()
        )

    def create(self, customer: Customer) -> Customer:
        self.db.add(customer)
        self.db.flush()
        return customer

    def update(self, customer: Customer) -> Customer:
        self.db.flush()
        return customer

    def delete(self, customer: Customer) -> None:
        self.db.delete(customer)
        self.db.flush()