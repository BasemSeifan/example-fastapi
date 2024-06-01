"""add content column to posts table

Revision ID: c8a0d320e805
Revises: 8838b284bb4c
Create Date: 2024-05-28 10:13:37.774070

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8a0d320e805'
down_revision: Union[str, None] = '8838b284bb4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')