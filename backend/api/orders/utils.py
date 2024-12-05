from fastapi import Body
from .schemas import OrderCreateSchema


def GetCreateItemData(
        order_in: OrderCreateSchema
) -> OrderCreateSchema:
    return OrderCreateSchema(
        order_number=order_in.order_number,
        address=order_in.address,
        delivery_type=order_in.delivery_type,
        payment_type=order_in.payment_type,
        isPaid=order_in.isPaid,
        customer_email=order_in.customer_email,
        customer_phone=order_in.customer_phone,
        cost_sum=order_in.cost_sum,
        items=order_in.items
    )