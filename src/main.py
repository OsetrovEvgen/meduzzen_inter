from fastapi import FastAPI
import uvicorn
from healthcheck.app import router

def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    return application

app = create_application()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000)
