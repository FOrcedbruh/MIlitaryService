"""add customer_name column to Order table

Revision ID: 979c6b93882d
Revises: a191fafaac5f
Create Date: 2024-12-12 11:47:13.192480

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '979c6b93882d'
down_revision: Union[str, None] = 'a191fafaac5f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('customer_name', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'customer_name')
    # ### end Alembic commands ###
