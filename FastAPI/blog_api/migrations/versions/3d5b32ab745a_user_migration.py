"""User migration

Revision ID: 3d5b32ab745a
Revises: a3e6d2e9a605
Create Date: 2025-02-25 20:43:00.014291

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3d5b32ab745a"
down_revision: Union[str, None] = "a3e6d2e9a605"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
