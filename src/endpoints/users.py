from fastapi import APIRouter, Depends
from repo.users import UserRepository
from .depends import get_users_repository


router = APIRouter()


@router.get('/')
async def read_users(users: UserRepository = Depends(get_users_repository), limit: int = 100, skip: int = 100):
    return await users.get_all(limit=limit, skip=skip)
