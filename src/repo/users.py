import datetime
from typing import List, Optional, Union, Any

import models.users
from security import hashed_password
from .base import BaseRepository
from db.users import User
from typing import List
from models.users import User as UserModel, UserInput
from sqlalchemy import update


class UserRepository(BaseRepository):
    async def get_all(self, limit: int = 20, page: int = 0) -> List[User]:
        res_users = []
        db_users = self.session.query(User).limit(limit).offset(page).all()
        return [UserModel.parse_obj(u.__dict__) for u in db_users]

    async def get_by_id(self, id: int) -> List[User]:
        res_users = []
        db_users = self.session.query(User).get(id)
        if User is None:
            return []
        else:
            return [UserModel.parse_obj(u.__dict__) for u in db_users]

    async def create(self, u: UserInput):
        res_users = []
        user = User(
            name=u.name,
            email=u.email,
            hashed_password=hashed_password(u.password),
            is_company=u.is_company,
            created_at=datetime.datetime.utcnow(),
        )
        self.session.add(user)
        self.session.commit()
        db_users = self.get_by_email(email=user.email)
        return db_users

    async def update(self, id: int, u: UserInput):
        res_users = []
        user = User(
            name=u.name,
            email=u.email,
            hashed_password=hashed_password(u.password),
            is_company=u.is_company,
            updated_att=datetime.datetime.utcnow()
        )
        values = {**user.__dict__}
        # values.pop('id', None)
        users = self.session.query(user.insert().values(**values))
        self.session.update(users)
        db_users = self.session.update(User.updated_at()).where(User.c.user == user)
        return [UserModel.parse_obj(u.__dict__) for u in db_users]

    async def get_by_email(self, email: str) -> Union[None, User]:
        res_user = self.session.query(User).filter_by(email=email).first()
        if res_user is None:
            return None
        else:
            return UserModel.parse_obj(res_user.__dict__)
