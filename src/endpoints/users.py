from repo.users import UserRepository
from .depends import get_users_repository, get_current_user
from pydantic import ValidationError
from fastapi import APIRouter, Depends, HTTPException, status
from models.users import UserInput, User
from typing import List, Optional


router = APIRouter()


@router.post('')
async def create_users(u: UserInput, users: UserRepository = Depends(get_users_repository)) -> User:
    try:
        return await users.create(u)
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid data fetched')


@router.get('')
async def read_all_users(email: str = "",
                         users: UserRepository = Depends(get_users_repository),
                         limit: int = 100,
                         page: int = 100) -> List[User]:
    try:
        if email != "" and not None:
            return await users.get_by_email(email=email)
        return await users.get_all(limit=limit, page=page)
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid data fetched')


@router.get('/{id}')
async def read_users_by_id(id: int, users: UserRepository = Depends(get_users_repository)) -> List[User]:
    try:
        return await users.get_by_id(id=id)
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')


@router.put('')
async def update_users(id: int,
                       u: UserInput,
                       users_repo: UserRepository = Depends(get_users_repository),
                       current_user: User = Depends(get_current_user)):
    print(current_user)
    print(id)
    print(current_user.id)
    print(id is current_user.id)
    print(type(id))
    print(type(current_user.id))
    if id == current_user.id:
        print('!')
        return users_repo.update(id=id, u=u)
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')


    # user = await users_repo.get_by_id(id=id)
    # if user is None or user[0].email != current_user.email:
    # #     return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found user')
    # try:
    #     return users_repo.update(id=id)
    # except ValidationError as e:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
