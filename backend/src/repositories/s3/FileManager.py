from botocore.exceptions import ClientError
from aiobotocore.session import get_session, AioSession
from .baseS3.AbstractS3Repository import AbstractS3Repository
from datetime import datetime
from contextlib import asynccontextmanager


class FileManager(AbstractS3Repository):
    def __init__(
        self,
        endpoint_url: str,
        access_key: str,
        secret_key: str,
        bucket_name: str
    ):
        self.config: dict = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url
        }
        self.bucket_name = bucket_name
        self.session: AioSession = get_session()
    
    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client

    async def upload_file(self, file):
        try:
            key: str = str(datetime.now()).replace(" ", "") + file.filename
            content = await file.read()
            async with self.get_client() as client:
                await client.put_object(Key=key, Body=content, Bucket=self.bucket_name)
        except ClientError as error:
            raise error

    async def delete_file(self, key):
        try: 
            async with self.get_client() as client:
                await client.delete_object(Key=key, Bucket=self.bucket_name)
        except ClientError as error:
            raise error
        
    