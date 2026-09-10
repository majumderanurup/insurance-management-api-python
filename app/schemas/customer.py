from datetime import date

from pydantic import BaseModel


class CustomerRequest(BaseModel):
    name: str
    email: str
    date_of_birth: date


class CustomerResponse(BaseModel):
    id: int
    name: str
    email: str
    date_of_birth: date