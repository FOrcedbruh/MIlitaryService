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
    
    async def delete_objects(
        self,
        filenames: list[str]
    ):
        try:
            objects_to_delete: list[dict] = []
            for filename in filenames:
                objects_to_delete.append({"Key": filename})
            
            async with self.get_client() as client:
                await client.delete_objects(Bucket=self.bucket_name, Delete={"Objects": objects_to_delete})
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Ошибка удаления файлов из s3 хранилища: {e}"
            )
        
        
        return {
            "status": status.HTTP_200_OK,
            "detail": "Успешное удаление файлов"
        }



s3_client = S3_Client(
    aws_access_key=settings.s3cfg.access_key,
    aws_secret_key=settings.s3cfg.secret_key,
    s3_url=settings.s3cfg.url,
    bucket_name=settings.s3cfg.bucketname
)
            