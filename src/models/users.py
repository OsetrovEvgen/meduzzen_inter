import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, validator


class User(BaseModel):
    id: Optional[int] = None
    name: str = None
    email: EmailStr = None
    hashed_password: str = None
    is_company: bool = None
    created_at: datetime.datetime = None
    updated_at: datetime.datetime = None


class UserInput(BaseModel):
    name: str
    email: EmailStr
    password: str
    password2: str
    is_company: bool = False

    @validator('password2')
    def password_math(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('Error password')
        return v
