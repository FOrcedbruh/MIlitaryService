from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from sqlalchemy import String, ARRAY
from sqlalchemy.ext.mutable import MutableList
from .order_items import order_items_association_table
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .item import Item

class Order(Base):
    __tablename__ = "orders"

    order_number: Mapped[str] = mapped_column(String(12), nullable=False, unique=True)
    cost_sum: Mapped[int]
    products: Mapped[list[str]] = mapped_column(MutableList.as_mutable(ARRAY(String)), nullable=False)
    address: Mapped[str] = mapped_column(nullable=False)
    delivery_type: Mapped[str] = mapped_column(nullable=False)
    payment_type: Mapped[str] = mapped_column(nullable=False)
    is_paid: Mapped[bool] = mapped_column(default=False)
    customer_phone: Mapped[str] = mapped_column(nullable=False)
    customer_email: Mapped[str] = mapped_column(nullable=False)
    customer_name: Mapped[str] = mapped_column(String(100), nullable=False)

    items: Mapped[list["Item"]] = relationship(back_populates="orders", secondary=order_items_association_table)