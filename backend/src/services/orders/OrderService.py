from dto.orders import OrderReadSchema, OrderCreateSchema, OrderReadSchemaAfterCreate
from repositories import OrdersRepository, ProductRepository
from models import Order

class OrderService():

    def __init__(self, repository: OrdersRepository):
        self.repository = repository

    async def get_order(self, order_id: int) -> OrderReadSchema:
        return await self.repository.get_one_with_products(order_id)
    
    async def create_order(
        self,
        order_in: OrderCreateSchema,
    ) -> OrderReadSchemaAfterCreate:
        order_to_create = Order(**order_in.model_dump(exclude="product_ids"))
        return await self.repository.create(order_in.product_ids, order_to_create)
    
    async def get_order_without_products(self, order_id: int) -> OrderReadSchema:
        return await self.repository.get_one(order_id)
    
    async def get_orders(self) -> list[OrderReadSchema]:
        return await self.repository.get_all()
