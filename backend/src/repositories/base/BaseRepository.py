from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar, Generic
from models import Base
from .exceptions import BaseException

ModelType = TypeVar(name="ModelType", bound=Base)
ExceptionType = TypeVar(name="ExceptionType", bound=BaseException)


class BaseRepository(Generic[ModelType]):
    
    def __init__(self, session: AsyncSession, model: ModelType, not_found_exception: ExceptionType):
        self.model = model
        self.session = session
        self.not_found_exception = not_found_exception
    
    async def list(self, offset: int, limit: int) -> list[ModelType]:
        query = select(self.model).offset(offset).limit(limit)
        stmt = await self.session.execute(query)
        res = stmt.scalars().all()
        if not res:
            raise self.not_found_exception
    
        return list(res)
    
    async def get_one(self, id: int) -> ModelType:
        res = await self.session.get(self.model, id)
        if res is None:
            raise self.not_found_exception
        
        return res
    
    async def create(self, data: ModelType) -> ModelType:
        self.session.add(data)
        await self.session.commit()
        await self.session.refresh(data)

        return data
    
    async def delete(self, id: int) -> None:
        res = await self.session.get(self.model, id)
        if res is None:
            raise self.not_found_exception
        
        await self.session.delete(res)
        await self.session.commit()
