from datetime import date
from decimal import Decimal

from pydantic import BaseModel

from app.models.policy import PolicyStatus


class DependentRequest(BaseModel):
    id: int


class DependentResponse(BaseModel):
    id: int
    name: str
    date_of_birth: date


class PolicyRequest(BaseModel):
    customer_id: int
    product_id: int
    start_date: date
    end_date: date
    sum_assured: Decimal
    premium: Decimal
    status: PolicyStatus = PolicyStatus.ACTIVE
    dependent_ids: list[int] = []


class PolicyResponse(BaseModel):
    id: int
    policy_number: str
    customer_id: int
    product_id: int
    start_date: date
    end_date: date
    sum_assured: Decimal
    premium: Decimal
    status: PolicyStatus
    dependents: list[DependentResponse] = []