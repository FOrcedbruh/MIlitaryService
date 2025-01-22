from pydantic import BaseModel, Field
from datetime import datetime


class OrderReadSchema(BaseModel):
    cost_sum: int
    order_number: str = Field(max_length=12)
    address: str
    delivery_type: str
    payment_type: str
    is_paid: bool
    customer_phone: str
    customer_email: str
    id: int
    created_at: datetime
    customer_name: str

