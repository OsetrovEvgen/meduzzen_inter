from repo.users import UserRepository
from .depends import get_users_repository
from pydantic import ValidationError
from fastapi import APIRouter, Depends, HTTPException, status
from models.users import UserInput, User

router = APIRouter()


@router.post('')
async def create_users(u: UserInput, users: UserRepository = Depends(get_users_repository)):
    try:
        return await users.create(u)
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid data fetched')


@router.get('')
async def read_all_users(email: str = "", users: UserRepository = Depends(get_users_repository), limit: int = 100, page: int = 100):
    try:
        if email != "" and not None:
            return await users.get_by_email(email=email)
        return await users.get_all(limit=limit, page=page)
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid data fetched')


@router.get('/{id}')
async def read_users_by_id(id: int, users: UserRepository = Depends(get_users_repository)):
    try:
        return await users.get_by_id(id=id)
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')


@router.put('')
async def update_users(id: int, users: UserRepository = Depends(get_users_repository)):
    try:
        return users.update(id=id)
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
