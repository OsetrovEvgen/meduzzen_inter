import datetime
from typing import List, Optional

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
        for u in db_users:
            res_users.append(UserModel.parse_obj(u.__dict__))
        return res_users

    async def get_by_id(self, id: int) -> List[User]:
        res_users = []
        db_users = self.session.query(User).get(id)
        if User is None:
            return []
        else:
            for u in db_users:
                res_users.append(UserModel.parse_obj(u.__dict__))
            return res_users

    async def create(self, u: UserInput):
        res_users = []
        user = User(
            name = u.name,
            email = u.email,
            hashed_password = hashed_password(u.password),
            is_company = u.is_company,
            created_at = datetime.datetime.utcnow(),
        )
        values = {**user.__dict__}
        values.pop('id', None)
        # users = UserInput(values)
        # users = self.session.query(user.().values(**values))
        # self.session.add(user)
        db_users = self.session.query(User.select()).where(User.c.user==user)
        for u in db_users:
            res_users.append(UserModel.parse_obj(u.__dict__))
        return res_users

    async def update(self, id: int, u: UserInput):
        res_users = []
        user = User(
            name = u.name,
            email = u.email,
            hashed_password = hashed_password(u.password),
            is_company = u.is_company,
            created_at = datetime.datetime.utcnow(),
            updated_att=datetime.datetime.utcnow()
        )
        values = {**user.dict()}
        values.pop('created_at', None)
        values.pop('id', None)
        users = self.session.query(user.insert().values(**values))
        self.session.update(users)
        db_users =self.session.update(User.updated_at()).where(User.c.user==user)
        for u in db_users:
            res_users.append(UserModel.parse_obj(u.__dict__))
        return res_users

    async def get_by_email(self, email: str) -> List[User]:
        res_users = []
        db_users = self.session.query(User.select()).where(User.c.email==email)
        if User is None:
            return []
        else:
            for u in db_users:
                res_users.append(UserModel.parse_obj(u.__dict__))
            return res_users

