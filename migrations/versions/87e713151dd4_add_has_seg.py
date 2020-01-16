"""add has_seg

Revision ID: 87e713151dd4
Revises: ce8081982e71
Create Date: 2020-01-16 14:18:42.991793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87e713151dd4'
down_revision = 'ce8081982e71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('qa', sa.Column('has_seg', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('qa', 'has_seg')
    # ### end Alembic commands ###