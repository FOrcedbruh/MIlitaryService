from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import OrderCreateSchema, OrderReadSchema
from core.models import Order, Item
from fastapi import status, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from . import utils
from .bot_api.utils import bot_utils

async def create_order(session: AsyncSession, order_in: OrderCreateSchema) -> dict:
    stmt = await session.execute(select(Item).where(Item.id.in_(order_in.item_ids)))
    items = stmt.scalars().all()

    if not items:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Товаров не найдено"
        )
    new_order = Order(**order_in.model_dump(exclude="item_ids"))
    new_order.items.extend(items)
    new_order.order_number = utils.generate_order_number()

    session.add(new_order)
    await session.commit()
    await session.refresh(new_order)

    res: dict = await bot_utils.send_new_order_to_bot(order_id=new_order.id, order_number=new_order.order_number)

    return {
        "status": status.HTTP_406_NOT_ACCEPTABLE,
        "detail": "Заказ успешно оформлен",
        "bot_message": res["message"]

    }

async def get_order(session: AsyncSession, order_id: int) -> OrderReadSchema:
    stmt = await session.execute(select(Order).options(selectinload(Order.items)).filter(Order.id == order_id))
    read_order = stmt.scalars().first()

    if not read_order:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Товар не найден"
        )
    
    return read_order



async def get_orders(session: AsyncSession) -> list[Order]:
    stmt = await session.execute(select(Order).options(selectinload(Order.items)))
    read_orders = stmt.scalars().all()

    if not read_orders:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Нет заказов"
        )
    
    return list(read_orders)

async def erase_order(session: AsyncSession, order_id: int) -> dict:
    order_to_erase = await session.get(Order, order_id)

    if not order_to_erase:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Заказ не найден"
        )
    
    await session.delete(order_to_erase)
    await session.commit()

    return {
        "status": status.HTTP_200_OK,
        "detail": "Товар успешно удален"
    }