from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .schemas import OrderCreateSchema
from core.models import Order
from fastapi import status


async def create_order(session: AsyncSession, order_in: OrderCreateSchema) -> dict:
    new_order = Order(**order_in.model_dump())

    session.add(new_order)

    await session.commit()


    return {
        "status": status.HTTP_201_CREATED,
        "detail": "Заказ успешно оформлен",
        "created_order": new_order
    }