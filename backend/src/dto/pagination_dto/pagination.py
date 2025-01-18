from pydantic import BaseModel


class PaginationSchema(BaseModel):
    limit: int = 100
    offset: int = 0