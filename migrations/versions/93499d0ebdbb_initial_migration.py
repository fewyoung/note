"""initial migration

Revision ID: 93499d0ebdbb
Revises: 383a4aac4377
Create Date: 2018-04-23 16:16:26.832973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93499d0ebdbb'
down_revision = '383a4aac4377'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('test2', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'test2')
    # ### end Alembic commands ###
