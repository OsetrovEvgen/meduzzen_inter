from fastapi import FastAPI
import uvicorn
from redis import Redis
from sqlalchemy import create_engine

from healthcheck.app import router
from config import settings


async def create_redis_connection():
    if Redis(host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        password=settings.REDIS_PASSWORD).ping():
        print("Redis connection accomplished")

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

def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    application.add_event_handler("startup", create_redis_connection)
    application.add_event_handler("startup", create_postgres_connection)
    return application

app = create_application()

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT)
