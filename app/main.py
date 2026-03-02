from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="S3 Storage Service",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "S3 Storage Service is running"}