from ..base.BaseRepository import BaseRepository
from models import Product
from .exceptions.exceptions import NotFoundProductException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class ProductRepository(BaseRepository[Product]):
    model = Product
    not_found_exception = NotFoundProductException()

    def __init__(self, session: AsyncSession):
        super().__init__(
            session=session,
            model=self.model, 
            not_found_exception=self.not_found_exception
        )

    async def update(self, data: dict, id: int) -> Product:
        res = await self.session.get(self.model, id)
        if res is None:
            raise self.not_found_exception
        
        for key, value in data.items():
            setattr(res, key, value)
        await self.session.commit()
        await self.session.refresh(res)

        return res

    async def add_images_urls(self, urls: list[str], id: int) -> Product:
        res = await self.session.get(self.model, id)
        if res is None:
            raise self.not_found_exception
        
        if res.images is None:
            res.images = urls
        else:
            res.images.extend(urls)
        
        await self.session.commit()
        await self.session.refresh(res)

        return res

    async def get_by_ids(self, ids: list[int]) -> list[Product]:
        query = select(self.model).where(self.model.id.in_(ids))
        stmt = await self.session.execute(query)
        res = stmt.scalars().all()

        if not res:
            raise self.not_found_exception

        return list(res)

    async def delete(self, id: int) -> list[str] | None:
        res = await self.session.get(self.model, id)
        if not res:
            raise self.not_found_exception
        
        await self.session.delete(res)
        await self.session.commit()
        
        return res.images