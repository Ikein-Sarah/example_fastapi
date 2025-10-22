"""merge heads

Revision ID: 1d46f4d88dfe
Revises: 1dbff25d5539, 1ef899227d71
Create Date: 2025-10-21 22:46:06.219581

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d46f4d88dfe'
down_revision: Union[str, Sequence[str], None] = ('1dbff25d5539', '1ef899227d71')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
