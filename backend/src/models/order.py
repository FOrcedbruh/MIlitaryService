from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from sqlalchemy import String, Enum
from .order_products import order_products_link_table
from typing import TYPE_CHECKING
from enum import StrEnum

if TYPE_CHECKING:
    from .product import Product

class DeliveryType(StrEnum):
    SDEK = "СДЭК"
    POCHTA = "ПОЧТА"
    DELLINES = "ДЕЛОВЫЕ ЛИНИИ"

class OrderStatus(StrEnum):
    PENDING = "PENDING"
    PAID = "PAID"
    FAILED = "FAILED"


class Order(Base):
    __tablename__ = "orders"

    order_number: Mapped[str] = mapped_column(String(12), nullable=False, unique=True)
    cost_sum: Mapped[int]
    address: Mapped[str] = mapped_column(nullable=False)
    delivery_type: Mapped[str] = mapped_column(nullable=False, default=DeliveryType.POCHTA)
    payment_type: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(nullable=True, default=OrderStatus.PENDING)
    customer_phone: Mapped[str] = mapped_column(nullable=False)
    customer_email: Mapped[str] = mapped_column(nullable=False)
    customer_name: Mapped[str] = mapped_column(String(100), nullable=False)

    products: Mapped[list["Product"]] = relationship(back_populates="orders", secondary=order_products_link_table)