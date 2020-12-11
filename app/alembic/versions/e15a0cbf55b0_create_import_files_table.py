"""create import_files table

Revision ID: e15a0cbf55b0
Revises: f1e346524572
Create Date: 2020-12-11 13:13:10.380073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e15a0cbf55b0'
down_revision = 'f1e346524572'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'import_files',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False),
        sa.Column('name', sa.String),
    )
    pass


def downgrade():
    pass
