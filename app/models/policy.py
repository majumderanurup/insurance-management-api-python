from datetime import date
from decimal import Decimal
from enum import Enum

from sqlalchemy import Date, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class PolicyStatus(str, Enum):
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    CANCELLED = "CANCELLED"


class Policy(Base):
    __tablename__ = "policies"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    policy_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True,
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id"),
        nullable=False,
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        nullable=False,
    )

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    end_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    sum_assured: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
    )

    premium: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
    )

    status: Mapped[PolicyStatus] = mapped_column(
        nullable=False,
        default=PolicyStatus.ACTIVE,
    )

    customer = relationship(
        "Customer",
    )

    product = relationship(
        "Product",
    )

    dependents = relationship(
        "Dependent",
        secondary="policy_dependents",
        back_populates="policies",
    )