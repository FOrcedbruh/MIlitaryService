from fastapi import Depends, Body, APIRouter, File, UploadFile, Query
from services import ProductService
from dependencies import get_product_service, get_product_s3
from dto.products import ProductReadSchema, ProductCreateSchema, ProductUpdateSchema
from repositories.s3 import ProductS3Repository
from dto.pagination_dto.pagination import PaginationSchema

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=list[ProductReadSchema])
async def index(
    pagination: PaginationSchema = Query(),
    service: ProductService = Depends(get_product_service)
) -> list[ProductReadSchema]:
    return await service.get_products(pagination)


@router.get("/{product_id}", response_model=ProductReadSchema)
async def index(
    product_id: int,
    service: ProductService = Depends(get_product_service)
) -> ProductReadSchema:
    return await service.get_product_by_id(product_id)


@router.post("/", response_model=ProductReadSchema)
async def index(
    product_in: ProductCreateSchema = Body(),
    service: ProductService = Depends(get_product_service)
) -> ProductReadSchema:
    return await service.create_product(product_in)


@router.patch("/{product_id}", response_model=ProductReadSchema)
async def index(
    product_id: int,
    product_in: ProductUpdateSchema = Body(),
    service: ProductService = Depends(get_product_service)
) -> ProductReadSchema:
    return await service.update_product(product_in, product_id)


@router.patch("/images-update/{product_id}", response_model=ProductReadSchema)
async def index(
    product_id: int,
    files: list[UploadFile] = File(),
    service: ProductService = Depends(get_product_service),
    s3: ProductS3Repository = Depends(get_product_s3)
) -> ProductReadSchema:
    return await service.update_images(product_id, files, s3)


@router.delete("/{product_id}", response_model=dict)
async def index(
    product_id: int,
    s3: ProductS3Repository = Depends(get_product_s3),
    service: ProductService = Depends(get_product_service)
) -> dict:
    return await service.delete_product(product_id, s3)