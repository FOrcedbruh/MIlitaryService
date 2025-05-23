"""correct error

Revision ID: cafc859cfb19
Revises: f3c263ec57fd
Create Date: 2025-04-11 13:16:29.616969

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cafc859cfb19'
down_revision: Union[str, None] = 'f3c263ec57fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('status', sa.String(), nullable=True))
    op.drop_column('orders', 'is_paid')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('is_paid', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('orders', 'status')
    # ### end Alembic commands ###
