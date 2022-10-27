from repo.users import UserRepository
from .depends import get_users_repository
from pydantic import ValidationError
from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter()

@router.get('/')
async def read_users(users: UserRepository = Depends(get_users_repository), id: int):
    try:
        return await users.get_by_id(id=id)
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
