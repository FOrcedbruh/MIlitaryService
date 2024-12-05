from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from .base import Base


class Order_Items(Base):
    __tablename__ = "order_items"

    item_id: Mapped[int] = mapped_column(ForeignKey("items.id", ondelete="CASCADE"), primary_key=True)

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id", ondelete="CASCADE"), primary_key=True)



