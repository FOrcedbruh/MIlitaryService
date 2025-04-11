from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from dto.products import ProductReadSchema
from models.order import OrderStatus, DeliveryType


class OrderReadSchemaAfterCreate(BaseModel):
    order_number: str
    cost_sum: int
    address: str
    order_number: str
    delivery_type: DeliveryType
    payment_type: str
    status: OrderStatus
    customer_phone: str
    customer_email: EmailStr
    customer_name: str = Field(max_length=100)

    
class OrderCreateSchema(BaseModel):
    cost_sum: int
    product_ids: list[int]
    address: str
    delivery_type: DeliveryType
    payment_type: str
    status: OrderStatus | None = None
    customer_phone: str
    customer_email: EmailStr
    customer_name: str = Field(max_length=100)

class OrderReadSchema(OrderCreateSchema):
    id: int
    order_number: str
    created_at: datetime
    products: list[ProductReadSchema] | None = None
    product_ids: None = None


class OrderReadInfoSchema(OrderReadSchema):
    products: list[str] | None = None
