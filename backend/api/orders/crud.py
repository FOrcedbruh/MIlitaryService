from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import OrderCreateSchema, OrderReadSchema
from core.models import Order, Item
from fastapi import status, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload


async def create_order(session: AsyncSession, order_in: OrderCreateSchema) -> dict:
    stmt = await session.execute(select(Item).where(Item.id.in_(order_in.item_ids)))
    items = stmt.scalars().all()

    if not items:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail="Товаров не найдено"
        )


    new_order = Order(**order_in.model_dump(exclude="item_ids"))
    new_order.items.extend(items)

    session.add(new_order)
    await session.commit()

    return {
        "status": status.HTTP_201_CREATED,
        "detail": "Заказ успешно оформлен",
        "created_order": new_order
    }

async def get_order(session: AsyncSession, order_id: int) -> OrderReadSchema:
    stmt = await session.execute(select(Order).options(selectinload(Order.items)).filter(Order.id == order_id))
    read_order = stmt.scalars().first()

    if not read_order:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail="Товар не найден"
        )
    
    return read_order

async def get_last_order(session: AsyncSession) -> Order:
    stmt = await session.execute(select(Order)
            .order_by(Order.id.desc()).limit(1)
                .options(selectinload(Order.items)))
    
    last_order = stmt.scalar()

    if not last_order:
        raise HTTPException(
            status_code=status.HTTP_200_OK,
            detail="Последний заказ не найден"
        )

    return last_order



async def get_orders(session: AsyncSession) -> list[Order]:
    stmt = await session.execute(select(Order))
    read_orders = stmt.scalars().all()

    if not read_orders:
        raise HTTPException(
            status_code=status.HTTP_200_OK,
            detail="Нет заказов"
        )
    
    return list(read_orders)