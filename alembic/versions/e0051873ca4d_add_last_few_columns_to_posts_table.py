"""add last few columns to posts table

Revision ID: e0051873ca4d
Revises: 94b45cd08964
Create Date: 2025-10-15 05:02:17.290878

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa,text


# revision identifiers, used by Alembic.
revision: str = 'e0051873ca4d'
down_revision: Union[str, Sequence[str], None] = '94b45cd08964'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default=text("true")))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("now()")))
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
