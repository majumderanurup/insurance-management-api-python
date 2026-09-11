import logging
from datetime import date
from decimal import Decimal

from sqlalchemy.orm import Session

from app.models.dependent import Dependent
from app.models.policy import Policy, PolicyStatus
from app.repositories.dependent_repository import DependentRepository
from app.repositories.policy_repository import PolicyRepository
from datetime import date

logger = logging.getLogger(__name__)


class PolicyService:

    def __init__(
        self,
        policy_repository: PolicyRepository,
        dependent_repository: DependentRepository,
        db: Session,
    ):
        self.policy_repository = policy_repository
        self.dependent_repository = dependent_repository
        self.db = db

    def _generate_policy_number(self) -> str:
        policy_count = self.policy_repository.get_count()

        return f"POL-{date.today().strftime('%Y%m%d')}-{policy_count + 1:06d}"

    def get_policies(self) -> list[Policy]:
        logger.info("Fetching all policies")

        return self.policy_repository.get_all()

    def get_policy(self, policy_id: int) -> Policy | None:
        logger.info(
            "Fetching policy with id: %s",
            policy_id,
        )

        return self.policy_repository.get_by_id(policy_id)

    def create_policy(
        self,
        customer_id: int,
        product_id: int,
        start_date: date,
        end_date: date,
        sum_assured: Decimal,
        premium: Decimal,
        status: PolicyStatus,
        dependent_ids: list[int],
    ) -> Policy:

        policy_number = self._generate_policy_number()

        logger.info(
            "Creating policy: %s",
            policy_number,
        )

        policy = Policy(
            policy_number=policy_number,
            customer_id=customer_id,
            product_id=product_id,
            start_date=start_date,
            end_date=end_date,
            sum_assured=sum_assured,
            premium=premium,
            status=status,
        )

        for dependent_id in dependent_ids:
            dependent = self.dependent_repository.get_by_id(
                dependent_id
            )

            if dependent is not None:
                policy.dependents.append(dependent)

        try:
            policy = self.policy_repository.create(policy)

            self.db.commit()
            self.db.refresh(policy)

            logger.info(
                "Policy created successfully with id: %s",
                policy.id,
            )

            return policy

        except Exception:
            self.db.rollback()

            logger.exception(
                "Failed to create policy: %s",
                policy_number,
            )

            raise

    def update_policy(
        self,
        policy_id: int,
        customer_id: int,
        product_id: int,
        start_date: date,
        end_date: date,
        sum_assured: Decimal,
        premium: Decimal,
        status: PolicyStatus,
        dependent_ids: list[int],
    ) -> Policy | None:

        logger.info(
            "Updating policy with id: %s",
            policy_id,
        )

        policy = self.policy_repository.get_by_id(policy_id)

        if policy is None:
            return None

        policy.customer_id = customer_id
        policy.product_id = product_id
        policy.start_date = start_date
        policy.end_date = end_date
        policy.sum_assured = sum_assured
        policy.premium = premium
        policy.status = status

        policy.dependents.clear()

        for dependent_id in dependent_ids:
            dependent = self.dependent_repository.get_by_id(
                dependent_id
            )

            if dependent is not None:
                policy.dependents.append(dependent)

        try:
            self.policy_repository.update(policy)

            self.db.commit()
            self.db.refresh(policy)

            logger.info(
                "Policy updated successfully with id: %s",
                policy_id,
            )

            return policy

        except Exception:
            self.db.rollback()

            logger.exception(
                "Failed to update policy with id: %s",
                policy_id,
            )

            raise

    def delete_policy(self, policy_id: int) -> bool:

        logger.info(
            "Deleting policy with id: %s",
            policy_id,
        )

        policy = self.policy_repository.get_by_id(policy_id)

        if policy is None:
            return False

        try:
            self.policy_repository.delete(policy)

            self.db.commit()

            logger.info(
                "Policy deleted successfully with id: %s",
                policy_id,
            )

            return True

        except Exception:
            self.db.rollback()

            logger.exception(
                "Failed to delete policy with id: %s",
                policy_id,
            )

            raise