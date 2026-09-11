from decimal import Decimal
from enum import Enum

from sqlalchemy import Boolean, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class ProductType(str, Enum):
    LIFE = "LIFE"
    HEALTH = "HEALTH"
    MOTOR = "MOTOR"
    TRAVEL = "TRAVEL"


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    type: Mapped[ProductType] = mapped_column(
        nullable=False,
    )

    min_entry_age: Mapped[int] = mapped_column(
        nullable=False,
    )

    max_entry_age: Mapped[int] = mapped_column(
        nullable=False,
    )

    min_sum_assured: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
    )

    max_sum_assured: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )