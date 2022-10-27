from repo.users import UserRepository
from .depends import get_users_repository
from pydantic import ValidationError
from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter()


@router.get('/')
async def read_users(users: UserRepository = Depends(get_users_repository), limit: int = 100, page: int = 100):
    try:
        return await users.get_all(limit=limit, page=page)
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid data fetched')

