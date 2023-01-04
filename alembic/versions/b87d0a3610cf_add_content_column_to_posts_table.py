"""add content column to posts table

Revision ID: b87d0a3610cf
Revises: c2410dded878
Create Date: 2023-01-03 15:31:18.619163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b87d0a3610cf'
down_revision = 'c2410dded878'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
