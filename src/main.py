from fastapi import FastAPI
import uvicorn
from config import settings
from db.base import databases

# from meduzzen_inter.src.db.base import databases

# from connection import create_redis_connection, create_postgres_connection
# from healthcheck.app import router
# from db.base import databases


app = FastAPI()


@app.get('/')
async def root():
    return {{'status': 'Working'}}


@app.on_event('startup')
async def startup():
    await databases.connect()


@app.on_event('shutdown')
async def shutdown():
    await databases.disconnect()

#
# def create_application() -> FastAPI:
#     application = FastAPI()
#     application.include_router(router)
#     application.add_event_handler("startup", create_redis_connection)
#     application.add_event_handler("startup", create_postgres_connection)
#     return application
#
# app = create_application()

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT, reload=True)
