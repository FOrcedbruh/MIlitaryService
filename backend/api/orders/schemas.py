from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from api.items.schemas import ItemReadSchema

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
    customer_name: str = Field(max_length=100)
    products: list[str]

class OrderReadSchema(OrderCreateSchema):
    id: int
    created_at: datetime
    items: list[ItemReadSchema]
    item_ids: None = None
    

class OrderInfoReadSchema(BaseModel):
    cost_sum: int
    order_number: str
    address: str
    delivery_type: str
    payment_type: str
    is_paid: bool
    customer_phone: str
    customer_email: str
    customer_name: str = Field(max_length=100)
    created_at: datetime
    products: list[str]