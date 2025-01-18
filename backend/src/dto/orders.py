from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from dto.products import ProductReadSchema


class OrderReadSchemaAfterCreate(BaseModel):
    order_number: str
    cost_sum: int
    address: str
    delivery_type: str
    payment_type: str
    is_paid: bool
    customer_phone: str
    customer_email: EmailStr
    customer_name: str = Field(max_length=100)

    
class OrderCreateSchema(BaseModel):
    order_number: str | None = None
    cost_sum: int
    product_ids: list[int] | None = None
    address: str
    delivery_type: str
    payment_type: str
    is_paid: bool
    customer_phone: str
    customer_email: EmailStr
    customer_name: str = Field(max_length=100)

class OrderReadSchema(OrderCreateSchema):
    id: int
    created_at: datetime
    products: list[ProductReadSchema] | None = None
    product_ids: None = None
    

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