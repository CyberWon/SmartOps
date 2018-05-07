"""empty message

Revision ID: 36b542c5b38
Revises: 3cb40a7a2f8
Create Date: 2018-03-28 14:30:34.602621

"""

# revision identifiers, used by Alembic.
revision = '36b542c5b38'
down_revision = '3cb40a7a2f8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password_hash', sa.String(length=164), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    ### end Alembic commands ###
