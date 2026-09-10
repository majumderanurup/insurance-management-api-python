from sqlalchemy.orm import Session

from app.models.customer import Customer


class CustomerRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Customer]:
        return self.db.query(Customer).all()