from fastapi import FastAPI
from typing import Union
import databases
from os import environ


# берем параметры БД из переменных окружения
DB_USER = environ.get("DB_USER", "user")
DB_PASSWORD = environ.get("DB_PASSWORD", "password")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_NAME = "async-blogs"
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)
# создаем объект database, который будет использоваться для выполнения запросов
database = databases.Database(SQLALCHEMY_DATABASE_URL)


app = FastAPI()


@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    await database.disconnect()


@app.get('/')
def root():
    return {"status": "Working"}

