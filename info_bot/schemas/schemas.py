from pydantic import BaseModel


class OrderInfoReadSchema(BaseModel):
    cost_sum: int
    order_number: str
    address: str
    delivery_type: str
    payment_type: str
    is_paid: bool
    customer_phone: str
    customer_email: str