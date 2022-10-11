import uvicorn


uvicorn.run(
    'healthcheck.app:app',
    reload=True
)
