import boto3
import uuid
from app.core.config import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_REGION,
    AWS_BUCKET_NAME,
)

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)


def upload_file(file, filename: str):
    unique_filename = f"{uuid.uuid4()}-{filename}"

    s3_client.upload_fileobj(
        file,
        AWS_BUCKET_NAME,
        unique_filename
    )

    return unique_filename


def generate_presigned_url(filename: str, expires_in=3600):
    url = s3_client.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": AWS_BUCKET_NAME,
            "Key": filename,
        },
        ExpiresIn=expires_in,
    )

    return url