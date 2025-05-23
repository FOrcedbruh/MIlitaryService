from dto.orders import OrderReadSchema, OrderCreateSchema, OrderReadSchemaAfterCreate, OrderReadInfoSchema
from repositories import OrdersRepository
from models import Order
from dto.pagination_dto.pagination import PaginationSchema
from .helpers.utils import generate_order_number
from utils.dadata.dadata_service import DadataService

class OrderService():

    def __init__(self, repository: OrdersRepository):
        self.repository = repository

    async def get_order(self, order_id: int) -> OrderReadSchema:
        return await self.repository.get_one_with_products(order_id)
    
    async def create_order(
        self,
        order_in: OrderCreateSchema
    ) -> OrderReadSchemaAfterCreate:
        order_to_create_dict: dict = order_in.model_dump(exclude="product_ids")
        order_to_create_dict["order_number"] = generate_order_number(order_in)
        order_to_create = Order(**order_to_create_dict)
        return await self.repository.create(order_in.product_ids, order_to_create)
    
    async def get_order_without_products(self, order_id: int) -> OrderReadSchema:
        return await self.repository.get_one(order_id)
    
    async def get_orders(self, pagination: PaginationSchema) -> list[OrderReadSchema]:
        return await self.repository.get_all(**pagination.model_dump(exclude_none=True))
    
    async def get_order_by_number(self, order_number: str) -> OrderReadInfoSchema:
        order = await self.repository.get_one_by_number(order_number)
        res = order.__dict__

        products = res["products"]
        products_names = []
        for product in products:
            products_names.append(product.name)
        res["products"] = products_names

        return res
    
    async def suggest_address(self, address_part: str) -> list:
        async with DadataService() as client:
            res = await client.suggest_address(address_part)
        return [x["value"] for x in res]

    
    async def get_all_order_numbers(self) -> list[str]:
        return await self.repository.get_numbers()
