from decimal import Decimal

from pydantic import BaseModel, Field

from app.models.product import ProductType


class ProductRequest(BaseModel):
    name: str = Field(max_length=100)
    description: str = Field(max_length=500)
    type: ProductType
    min_entry_age: int
    max_entry_age: int
    min_sum_assured: Decimal
    max_sum_assured: Decimal
    active: bool = True


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    type: ProductType
    min_entry_age: int
    max_entry_age: int
    min_sum_assured: Decimal
    max_sum_assured: Decimal
    active: bool