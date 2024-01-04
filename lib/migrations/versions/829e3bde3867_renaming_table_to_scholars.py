"""renaming table to scholars

Revision ID: 829e3bde3867
Revises: 791279dd0760
Create Date: 2024-01-04 21:01:24.470277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '829e3bde3867'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
