from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class PolicyDependent(Base):
    __tablename__ = "policy_dependents"

    policy_id: Mapped[int] = mapped_column(
        ForeignKey("policies.id"),
        primary_key=True,
    )

    dependent_id: Mapped[int] = mapped_column(
        ForeignKey("dependents.id"),
        primary_key=True,
    )