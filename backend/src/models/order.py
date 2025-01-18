from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from sqlalchemy import String
from .order_products import order_products_link_table
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .product import Product

class Order(Base):
    __tablename__ = "orders"

    order_number: Mapped[str] = mapped_column(String(12), nullable=False, unique=True)
    cost_sum: Mapped[int]
    address: Mapped[str] = mapped_column(nullable=False)
    delivery_type: Mapped[str] = mapped_column(nullable=False)
    payment_type: Mapped[str] = mapped_column(nullable=False)
    is_paid: Mapped[bool] = mapped_column(default=False)
    customer_phone: Mapped[str] = mapped_column(nullable=False)
    customer_email: Mapped[str] = mapped_column(nullable=False)
    customer_name: Mapped[str] = mapped_column(String(100), nullable=False)

    products: Mapped[list["Product"]] = relationship(back_populates="orders", secondary=order_products_link_table)