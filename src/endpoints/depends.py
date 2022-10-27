from repo.users import UserRepository
from db.base import session


def get_users_repository() -> UserRepository:
    return UserRepository(session)
