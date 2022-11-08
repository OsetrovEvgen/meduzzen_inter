from fastapi import Depends, HTTPException, status
from repo.users import UserRepository
from db.base import session
from security import JWTBearer, decode_access_token
from models.users import User
from typing import Any


def get_users_repository() -> UserRepository:
    return UserRepository(session)


async def get_current_user(
        users: UserRepository = Depends(get_users_repository),
        token: str = Depends(JWTBearer())):
    cred_exeption = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Credentials are not valid')
    payload = decode_access_token(token)
    if payload is None:
        raise cred_exeption
    email: str = payload.get('sub')
    if email is None:
        raise cred_exeption
    user = await users.get_by_email(email=email)
    if user is None:
        return cred_exeption
    return user

