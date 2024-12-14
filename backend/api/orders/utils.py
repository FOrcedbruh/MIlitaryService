from fastapi import Body
from .schemas import OrderCreateSchema
import random



def GetCreateItemData(
    order_in: OrderCreateSchema
) -> OrderCreateSchema:
    return OrderCreateSchema(
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


def generate_order_number() -> str:
    x: list[str] = ["1", "2", "3", "4", "5", "6", "7", "8"]
    random.shuffle(x=x)
    return "".join(x)