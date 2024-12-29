from ...schemas import OrderInfoReadSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import Order
from fastapi import HTTPException, status
from ..utils.bot_utils import order_response_for_bot


async def get_orders_for_info(session: AsyncSession) -> list[OrderInfoReadSchema]:
    stmt = await session.execute(select(Order))
    read_orders = stmt.scalars().all()


    if not read_orders:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail="Нет заказов"
        )
    
    response_orders: list[OrderInfoReadSchema] = []
    for order in read_orders:
        response_orders.append(order_response_for_bot(order_in=order)
    )
        
    return response_orders
    
    



async def get_last_order(session: AsyncSession) -> OrderInfoReadSchema:
    stmt = await session.execute(select(Order)
            .order_by(Order.id.desc()).limit(1))
    
    last_order = stmt.scalar()

    if not last_order:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail="Последний заказ не найден"
        )

    return order_response_for_bot(order_in=last_order)


async def get_order_for_bot_by_id(session: AsyncSession, order_id: int) -> OrderInfoReadSchema:
    order = await session.get(Order, order_id)

    if not order:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Заказ не найден"
        )
    
    return order_response_for_bot(order_in=order)