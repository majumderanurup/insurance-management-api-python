from sqlalchemy.orm import Session

from app.models.policy import Policy


class PolicyRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Policy]:
        return self.db.query(Policy).all()

    def get_by_id(self, policy_id: int) -> Policy | None:
        return (
            self.db.query(Policy)
            .filter(Policy.id == policy_id)
            .first()
        )

    def get_by_policy_number(
        self,
        policy_number: str,
    ) -> Policy | None:
        return (
            self.db.query(Policy)
            .filter(Policy.policy_number == policy_number)
            .first()
        )

    def get_count(self) -> int:
        return self.db.query(Policy).count()

    def create(self, policy: Policy) -> Policy:
        self.db.add(policy)
        self.db.flush()
        return policy

    def update(self, policy: Policy) -> Policy:
        self.db.flush()
        return policy

    def delete(self, policy: Policy) -> None:
        self.db.delete(policy)
        self.db.flush()