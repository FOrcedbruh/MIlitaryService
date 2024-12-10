from pydantic import BaseModel



class ItemSchema(BaseModel):
    id: int
    title: str
    description: str


class OrderSchema(BaseModel):
    items: list[ItemSchema]
    order_number: str
    cost_sum: int
    address: str
    delivery_type: str
    payment_type: str
    isPaid: int
    customer_phone: str
    customer_email: str