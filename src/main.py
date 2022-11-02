from fastapi import FastAPI
import uvicorn
from config import settings
from connection import create_redis_connection, create_postgres_connection
from healthcheck.app import router
from endpoints import users, auth


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    application.add_event_handler("startup", create_postgres_connection)
    application.add_event_handler("startup", create_redis_connection)
    return application

app = create_application()
app.include_router(users.router, prefix='/users', tags=['users'])
app.include_router(auth.router, prefix='/auth', tags=['auth'])


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT, reload=True)
