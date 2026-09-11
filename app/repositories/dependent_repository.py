from sqlalchemy.orm import Session

from app.models.dependent import Dependent


class DependentRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, dependent_id: int) -> Dependent | None:
        return (
            self.db.query(Dependent)
            .filter(Dependent.id == dependent_id)
            .first()
        )

    def get_by_customer(
        self,
        customer_id: int,
    ) -> list[Dependent]:
        return (
            self.db.query(Dependent)
            .filter(Dependent.customer_id == customer_id)
            .all()
        )

    def create(self, dependent: Dependent) -> Dependent:
        self.db.add(dependent)
        self.db.flush()
        return dependent