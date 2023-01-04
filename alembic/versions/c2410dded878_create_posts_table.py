"""create posts table

Revision ID: c2410dded878
Revises: 
Create Date: 2023-01-03 15:17:06.384882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2410dded878'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    
    pass

def downgrade() -> None:
    op.drop_table('posts')
    pass
