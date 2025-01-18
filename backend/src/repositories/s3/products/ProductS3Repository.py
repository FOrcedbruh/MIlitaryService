from ..FileManager import FileManager
from datetime import datetime
from botocore.exceptions import ClientError
from core.config import settings

class ProductS3Repository(FileManager):
    
    def __init__(self, endpoint_url: str, access_key: str, secret_key: str, bucket_name: str):
        super().__init__(endpoint_url, access_key, secret_key, bucket_name)


    async def upload_images(self, images: list) -> list[str]:
        res: list[str] = []
        try:
            async with super().get_client() as client:
                for image in images:
                    key: str = str(datetime.now).replace(" ", "") + image.filename
                    res.append(settings.s3cfg.get_url + "/" + key)
                    content = await image.read()
                    await client.put_object(Key=key, Body=content, Bucket=self.bucket_name)
        except ClientError as error:
            raise error
        
        return res

    async def delete_images(self, keys: list[str]) -> int:
        try:
            images_to_delete: list[dict] = []
            for key in keys:
                    images_to_delete.append({"Key": key})
            async with super().get_client() as client:
                await client.delete_objects(Bucket=self.bucket_name, Delete={"Objects": images_to_delete})

        except ClientError as error:
            raise error
        
        return len(keys)