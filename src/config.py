from pydantic import BaseSettings, SecretStr
from starlette.config import Config


config = Config('.env')

DATABASE_URL = config('MED_DATABASE_URL', cast=str, default='')


class Settings(BaseSettings):
    class Config:
        env_file = '../.env'

    SERVER_PORT: int
    SERVER_HOST: str

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int
    POSTGRES_HOST: str
    POSTGRES_DB: str

settings = Settings()
