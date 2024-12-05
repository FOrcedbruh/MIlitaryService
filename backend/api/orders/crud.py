from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import OrderCreateSchema
from core.models import Order, Item
from fastapi import status
from sqlalchemy import select


async def create_order(session: AsyncSession, order_in: OrderCreateSchema) -> dict:
    stmt = await session.execute(select(Item).where(Item.id.in_(order_in.item_ids)))
    items = stmt.scalars().all()


    new_order = Order(**order_in.model_dump(exclude="item_ids"))
    new_order.items.extend(items)

    session.add(new_order)
    await session.commit()

    return new_order

    

    