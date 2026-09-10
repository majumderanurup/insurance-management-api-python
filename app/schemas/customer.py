from datetime import date

from pydantic import BaseModel, EmailStr, Field, field_validator


class CustomerRequest(BaseModel):
    name: str = Field(max_length=100)
    email: EmailStr
    date_of_birth: date

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        value = value.strip()

        if len(value) < 2:
            raise ValueError("Name must contain at least 2 characters")

        return value

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: EmailStr) -> str:
        return str(value).strip().lower()

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, value: date) -> date:
        if value > date.today():
            raise ValueError("Date of birth cannot be in the future")
        return value


class CustomerResponse(BaseModel):
    id: int
    name: str
    email: str
    date_of_birth: date