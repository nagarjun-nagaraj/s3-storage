from fastapi import FastAPI

app = FastAPI(
    title="S3 Storage Service",
    version="1.0.0",
)
@app.get("/")
def root():
    return {"message": "S3 Storage Service is running"}