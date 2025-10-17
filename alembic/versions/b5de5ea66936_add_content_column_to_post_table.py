"""add content column to post table

Revision ID: b5de5ea66936
Revises: 331ca6e4b74f
Create Date: 2025-10-14 14:18:16.960988

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b5de5ea66936'
down_revision: Union[str, Sequence[str], None] = '331ca6e4b74f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
