from fastapi import FastAPI
import uvicorn
from config import settings
from connection import create_redis_connection, create_postgres_connection
from healthcheck.app import router
from db.base import metadata, engine


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    application.add_event_handler("startup", create_postgres_connection)
    application.add_event_handler("startup", create_redis_connection)
    metadata.create_all(bind=engine)
    return application

app = create_application()

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT, reload=True)
