from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ARRAY
from sqlalchemy.ext.mutable import MutableList

class Item(Base):
    __tablename__ = "items"

    item_name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(500))
    limit: Mapped[int] = mapped_column(nullable=False)
    cost: Mapped[int] = mapped_column(nullable=False)
    images: Mapped[list[str]] = mapped_column(MutableList.as_mutable(ARRAY(String)), nullable=False)