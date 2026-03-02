from fastapi import APIRouter, UploadFile, File
from app.services.s3 import upload_file

router = APIRouter()


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    file_url = upload_file(file.file, file.filename)

    return {
        "filename": file.filename,
        "url": file_url
    }