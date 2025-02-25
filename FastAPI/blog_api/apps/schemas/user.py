import datetime

from email_validator import EmailNotValidError, validate_email
from pydantic import BaseModel, Field, field_validator


class UserBase(BaseModel):
    name: str = Field(..., min_length=1, strip_whitespace=True)
    email: str = Field(..., strip_whitespace=True)

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        try:
            validate_email(value)
        except EmailNotValidError:
            raise ValueError("Invalid email format")
        return value


class UserCreate(UserBase):
    password: str = Field(..., min_length=1, strip_whitespace=True)


class UserUpdate(BaseModel):
    name: str = Field(..., min_length=1, strip_whitespace=True)


class UserResponse(UserBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
