import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, validator


class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: EmailStr
    hashed_password: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

class UserInput(BaseModel):
    name: str
    email: EmailStr
    password: str
    password2: str
    is_company: bool = False

    @validator('password')
    def password_math(self, cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('Error password')
        return v
