"""Add m2m order_items

Revision ID: 9ed68c86099c
Revises: 619733f8cd47
Create Date: 2024-12-05 09:16:49.423575

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ed68c86099c'
down_revision: Union[str, None] = '619733f8cd47'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('order_number', sa.String(length=12), nullable=False),
    sa.Column('cost_sum', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('delivery_type', sa.String(), nullable=False),
    sa.Column('payment_type', sa.String(), nullable=False),
    sa.Column('is_paid', sa.Boolean(), nullable=False),
    sa.Column('customer_phone', sa.String(), nullable=False),
    sa.Column('customer_email', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('order_number')
    )
    op.create_table('order_items',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('item_id', 'order_id', 'id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_items')
    op.drop_table('orders')
    # ### end Alembic commands ###