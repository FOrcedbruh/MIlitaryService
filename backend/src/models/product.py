from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ARRAY
from sqlalchemy.ext.mutable import MutableList
from .order_products import order_products_link_table
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .order import Order



class Product(Base):
    __tablename__ = "products"

    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(500))
    limit: Mapped[int] = mapped_column(nullable=False)
    cost: Mapped[int] = mapped_column(nullable=False)
    images: Mapped[list[str]] = mapped_column(MutableList.as_mutable(ARRAY(String)), nullable=True)

    orders: Mapped[list["Order"]] = relationship(back_populates="products", secondary=order_products_link_table)