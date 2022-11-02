from repo.users import UserRepository
from db.base import databases


def get_users_repository(databases) -> UserRepository:
    return UserRepository(databases)
