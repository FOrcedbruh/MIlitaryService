from sqlalchemy import Table, Column, ForeignKey, Integer
from .base import Base


order_items_association_table = Table(
    "order_items_association",
    Base.metadata,
    Column("order_id", ForeignKey("orders.id"), nullable=False),
    Column("item_id", ForeignKey("items.id"), nullable=False),
    Column("id", Integer, primary_key=True)
)




