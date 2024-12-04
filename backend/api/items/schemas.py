from pydantic import BaseModel, Field
from datetime import datetime


class ItemCreateSchema(BaseModel):
    item_name: str
    description: str = Field(max_length=500)
    limit: int
    cost: int
    images: list[str]

class ItemReadSchema(ItemCreateSchema):
    id: int
    created_at: datetime

class ItemUpdateSchema(BaseModel):
    item_name: str | None = None
    description: str | None = None
    limit: int | None = None
    cost: int | None = None
    images: list[str] | None = None