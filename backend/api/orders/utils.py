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
        is_paid=order_in.is_paid,
        customer_email=order_in.customer_email,
        customer_phone=order_in.customer_phone,
        cost_sum=order_in.cost_sum,
        item_ids=order_in.item_ids,
        customer_name=order_in.customer_name,
        products=order_in.products
    )