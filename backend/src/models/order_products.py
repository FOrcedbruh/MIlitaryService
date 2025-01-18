from sqlalchemy import Table, Column, ForeignKey, Integer
from .base import Base


order_products_link_table = Table(
    "orders_products_link",
    Base.metadata,
    Column("order_id", ForeignKey("orders.id"), nullable=False),
    Column("product_id", ForeignKey("products.id"), nullable=False),
    Column("id", Integer, primary_key=True)
)




