from pydantic import BaseModel, Field, EmailStr
from datetime import datetime


class OrderCreateSchema(BaseModel):
    order_number: str = Field(min_length=8)
    cost_sum: int
    item_ids: list[int]
    address: str
    delivery_type: str
    payment_type: str
    is_paid: bool
    customer_phone: str
    customer_email: EmailStr

class OrderReadSchema(OrderCreateSchema):
    id: int
    created_at: datetime
