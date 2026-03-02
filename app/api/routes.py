from fastapi import APIRouter, UploadFile, File
from app.services.s3 import upload_file, generate_presigned_url

router = APIRouter()


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    filename = upload_file(file.file, file.filename)
    url = generate_presigned_url(filename)

    return {
        "filename": filename,
        "url": url
    }