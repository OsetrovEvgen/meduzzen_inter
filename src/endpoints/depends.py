from repo.users import UserRepository
from db.base import databases


def get_users_repository() ->UserRepository:
    return UserRepository(databases)
