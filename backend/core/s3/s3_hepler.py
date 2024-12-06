from aiobotocore.session import get_session
from core.settings import settings
from contextlib import asynccontextmanager
from fastapi import UploadFile, HTTPException, status

class S3_Client():
    def __init__(
            self, 
            aws_secret_key: str,
            aws_access_key: str,
            s3_url: str,
            bucket_name: str
        ):
            self.config: dict = {
                "aws_access_key_id": aws_access_key,
                "aws_secret_access_key": aws_secret_key,
                "endpoint_url": s3_url
            }

            self.bucket_name: str = bucket_name
            self.session = get_session()
    

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as session:
            yield session

    async def put_files(
        self,
        images: list[UploadFile]
    ):
        try:
            async with self.get_client() as client:
                for image in images:
                    content: str = await image.read()
                    filename: str = image.filename
                    await client.put_object(Key=filename, Body=content, Bucket=self.bucket_name)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Ошибка загрузки файла в s3 хранилище: {e}"
            )
        
        return {
            "status": status.HTTP_201_CREATED,
            "detail": f"Успешна загрузка файла {filename}"
        }
    


s3_client = S3_Client(
    aws_access_key=settings.s3cfg.access_key,
    aws_secret_key=settings.s3cfg.secret_key,
    s3_url=settings.s3cfg.url,
    bucket_name=settings.s3cfg.bucketname
)
            