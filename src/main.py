from fastapi import FastAPI
import uvicorn
from config import settings
# from base import database

from connection import create_redis_connection, create_postgres_connection
from healthcheck.app import router

from db.users import users
from db.base import metadata, engine

#
# app = FastAPI()

#
# @app.get('/')
# async def root():
#     return {{'status': 'Working'}}
#
#
# @app.on_event('startup')
# async def startup():
#     await database.connect()
#
#
# @app.on_event('shutdown')
# async def shutdown():
#     await database.disconnect()
#





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
