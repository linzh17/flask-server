"""empty message

Revision ID: 3acd9b394fd8
Revises: 60424aea1a23
Create Date: 2018-09-26 21:09:56.764542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3acd9b394fd8'
down_revision = '60424aea1a23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('Userid', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('nickName', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.Column('avatarUrl', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('Userid')
    )
    op.create_table('localusers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=64), nullable=True),
    sa.Column('Userid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Userid'], ['users.Userid'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('localusers')
    op.drop_table('users')
    # ### end Alembic commands ###
