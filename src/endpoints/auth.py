from fastapi import APIRouter, Depends, HTTPException, status
from models.token import Token, Login
from repo.users import UserRepository
from .depends import get_users_repository
from security import verify_password, create_access_token

router = APIRouter()


@router.post('/', response_model=Token)
async def login(login: Login, users: UserRepository = Depends(get_users_repository)) ->Token:
    user = await users.get_by_email(login.email)
    if user is None or not verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password')
    return Token(
        access_token=create_access_token({'sub': user.email}),
        token_type='Bearer'
    )
