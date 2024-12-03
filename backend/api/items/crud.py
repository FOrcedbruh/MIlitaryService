from fastapi import status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import Item
from . import utils
from .schemas import ItemCreateSchema



async def create_item(session: AsyncSession, item_in: ItemCreateSchema) -> dict:
    stmt = await session.execute(select(Item).filter(Item.item_name == item_in.item_name))
    item = stmt.scalars().first()

    if item:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Такой товар уже существует"
        )
    
    new_item = Item(**item_in.model_dump())

    session.add(new_item)
    await session.commit()

    return {
        "status": status.HTTP_201_CREATED,
        "detail": "Товар усвешно добавлен",
        "created_item": new_item
    }
    