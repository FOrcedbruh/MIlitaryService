from  ..base.BaseRepository import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from models import Order, Product
from .exceptions.exceptions import NotFoundOrderException
from sqlalchemy.orm import selectinload
from sqlalchemy import select



class OrdersRepository(BaseRepository[Order]):
    model = Order
    not_found_exception = NotFoundOrderException()

    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model=self.model, not_found_exception=self.not_found_exception)

    async def get_one_with_products(self, id: int) -> Order:
        query = select(self.model).options(selectinload(self.model.products)).where(self.model.id == id)
        stmt = await self.session.execute(query)
        res = stmt.scalar_one_or_none()
        if res is None:
            raise self.not_found_exception
        
        return res
    
    async def create(self, ids: list[int], data: Order) -> Order:
        query = select(Product).where(Product.id.in_(ids))
        stmt = await self.session.execute(query)
        res = stmt.scalars().all()

        data.products.extend(res)
        self.session.add(data)
        await self.session.commit()
        await self.session.refresh(data)

        return data
    
    async def get_all(self, offset: int, limit: int) -> list[Order]:
        query = select(self.model).offset(offset).limit(limit).options(selectinload(self.model.products))
        stmt = await self.session.execute(query)
        res = stmt.scalars().all()
        if not res:
            raise self.not_found_exception
        return list(res)
    
    async def get_one_by_number(self, data: str) -> Order:
        query = select(self.model).where(self.model.order_number == data).options(selectinload(self.model.products))
        stmt = await self.session.execute(query)
        res = stmt.scalar_one_or_none()

        if res is None:
            raise self.not_found_exception
        
        return res
        


