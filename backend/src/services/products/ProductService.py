from repositories import ProductRepository
from dto.products import ProductCreateSchema, ProductReadSchema, ProductUpdateSchema
from models import Product
from repositories.s3 import ProductS3Repository
from dto.pagination_dto.pagination import PaginationSchema
from core.config import settings



class ProductService():
    
    def __init__(self, repository: ProductRepository):
        self.repository = repository


    async def get_products(self, pagination: PaginationSchema) -> list[ProductReadSchema]:
        return await self.repository.list(**pagination.model_dump(exclude_none=True))
    

    async def get_product_by_id(self, product_id: int) -> ProductReadSchema:
        return await self.repository.get_one(product_id)


    async def create_product(self, product_in: ProductCreateSchema) -> ProductReadSchema:
        item_to_create = Product(**product_in.model_dump(exclude_none=True))
        return await self.repository.create(item_to_create)
    

    async def update_product(self, product_in: ProductUpdateSchema, product_id: int) -> ProductReadSchema:
        return await self.repository.update(product_in.model_dump(exclude_none=True), product_id)
    

    async def delete_product(self, product_id: int, s3: ProductS3Repository) -> dict:
        urls = await self.repository.delete(product_id)
        keys: list[str] = []
        for url in urls:
            keys.append(url[settings.s3cfg.len_get_s3_url+1:])

        if keys is not None:
            await s3.delete_images(keys)

        return {
            "message": "Товар успешно удален"
        }

    async def update_images(self, product_id: int, files, s3: ProductS3Repository) -> ProductReadSchema:
        urls: list[str] = await s3.upload_images(images=files)
        return await self.repository.add_images_urls(urls, product_id)
    
    async def delete_images(self, product_id: int, keys: list[str], s3: ProductS3Repository) -> ProductReadSchema:
        ...