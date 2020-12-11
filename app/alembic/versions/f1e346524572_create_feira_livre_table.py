"""create feira_livre table

Revision ID: f1e346524572
Revises: 
Create Date: 2020-12-11 13:07:54.875098

"""
from alembic import op
from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy as sa
import uuid

# revision identifiers, used by Alembic.
revision = 'f1e346524572'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'feira_livre',
        sa.Column('uuid', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False),
        sa.Column('id', sa.Integer),
        sa.Column('long', sa.String),
        sa.Column('lat', sa.String),
        sa.Column('setcens', sa.String),
        sa.Column('areap', sa.String),
        sa.Column('coddist', sa.String),
        sa.Column('distrito', sa.String),
        sa.Column('codsubpref', sa.String),
        sa.Column('subprefe', sa.String),
        sa.Column('regiao5', sa.String),
        sa.Column('regiao8', sa.String),
        sa.Column('nome_feira', sa.String),
        sa.Column('registro', sa.String),
        sa.Column('logradouro', sa.String),
        sa.Column('numero', sa.String),
        sa.Column('bairro', sa.String),
        sa.Column('referencia', sa.String),
    )
    pass


def downgrade():
    pass
