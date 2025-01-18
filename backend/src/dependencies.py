from fastapi import Depends
from core.database.DataBaseConnections import DatabaseConnection
from core.config import settings
from sqlalchemy.ext.asyncio import AsyncSession
from repositories import ProductRepository, OrdersRepository
from services import ProductService, OrderService
from repositories.s3 import ProductS3Repository

def get_db_connection() -> DatabaseConnection:
    return DatabaseConnection(
        db_url=settings.dbcfg.url,
        echo=settings.dbcfg.echo,
        pool_size=settings.dbcfg.pool_size
    )

def get_product_repository(
    session: AsyncSession = Depends(get_db_connection().generate_session)
) -> ProductRepository:
    return ProductRepository(session=session)

def get_product_service(
    repository: ProductRepository = Depends(get_product_repository)
) -> ProductService:
    return ProductService(repository=repository)
    
def get_order_repository(
    session: AsyncSession = Depends(get_db_connection().generate_session)
) -> OrdersRepository:
    return OrdersRepository(session=session)

def get_order_service(
    repository: OrdersRepository = Depends(get_order_repository)
) -> OrderService:
    return OrderService(repository=repository)

def get_product_s3() -> ProductS3Repository:
    return ProductS3Repository(
        endpoint_url=settings.s3cfg.url,
        access_key=settings.s3cfg.access_key,
        secret_key=settings.s3cfg.secret_key,
        bucket_name=settings.s3cfg.bucketname
    )
    