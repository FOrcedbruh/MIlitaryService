from pydantic import BaseModel, Field
from datetime import datetime


class ProductCreateSchema(BaseModel):
    name: str
    description: str = Field(max_length=500)
    limit: int
    cost: int

class ProductReadSchema(ProductCreateSchema):
    id: int
    created_at: datetime
    images: list[str]
    

class ProductUpdateSchema(BaseModel):
    name: str | None = None
    description: str | None = None
    limit: int | None = None
    cost: int | None = None