import redis
from sqlalchemy import create_engine
from config import settings


async def create_postgres_connection():
    create_engine("postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(
            settings.POSTGRES_USER,
            settings.POSTGRES_PASSWORD,
            settings.POSTGRES_HOST,
            settings.POSTGRES_PORT,
            settings.POSTGRES_DB
        )
    )
    print("PostgreSQL connection accomplished")


async def create_redis_connection():
    return redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

