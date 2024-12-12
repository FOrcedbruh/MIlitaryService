from ..schemas import OrderInfoReadSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import Order
from fastapi import HTTPException, status



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
        response_orders.append(OrderInfoReadSchema(
        order_number=order.order_number,
        cost_sum=order.cost_sum,
        address=order.address,
        delivery_type=order.delivery_type,
        payment_type=order.payment_type,
        is_paid=order.is_paid,
        customer_email=order.customer_email,
        customer_phone=order.customer_phone,
        customer_name=order.customer_name,
        products=order.products,
        created_at=order.created_at
    ))
        
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

    return OrderInfoReadSchema(
        order_number=last_order.order_number,
        cost_sum=last_order.cost_sum,
        address=last_order.address,
        delivery_type=last_order.delivery_type,
        payment_type=last_order.payment_type,
        is_paid=last_order.is_paid,
        customer_email=last_order.customer_email,
        customer_phone=last_order.customer_phone,
        customer_name=last_order.customer_name,
        products=last_order.products,
        created_at=last_order.created_at
    )
    