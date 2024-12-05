from pydantic import BaseModel, Field, EmailStr
from datetime import datetime


class OrderCreateSchema(BaseModel):
    order_number: str = Field(20)
    cost_sum: int
    items: list[int]
    address: str
    delivery_type: str
    payment_type: str
    isPaid: bool
    items: list[int]
    customer_phone: str
    customer_email: EmailStr

class OrderReadSchema(OrderCreateSchema):
    id: int
    created_at: datetime
