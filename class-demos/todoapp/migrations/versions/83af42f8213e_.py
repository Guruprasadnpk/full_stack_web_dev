"""empty message

Revision ID: 83af42f8213e
Revises: e7ae30469b45
Create Date: 2021-01-09 21:22:04.154591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83af42f8213e'
down_revision = 'e7ae30469b45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
