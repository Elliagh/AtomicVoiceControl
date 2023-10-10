"""Database creation

Revision ID: 1cee6d2ebcf4
Revises: 
Create Date: 2023-10-10 22:53:27.831419

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '1cee6d2ebcf4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('location', sa.String(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('sign', sa.String(), nullable=True),
                    sa.Column('Battery', sa.Integer(), nullable=True),
                    sa.Column('Type', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('firstname', sa.String(), nullable=True),
                    sa.Column('secondname', sa.String(), nullable=True),
                    sa.Column('location', sa.String(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('address', sa.String(), nullable=True),
                    sa.Column('number', sa.Integer(), nullable=True),
                    sa.Column('car_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['car_id'], ['cars.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('register',
                    sa.Column('token', sa.String(), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('last_registration', sa.TIMESTAMP(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('register')
    op.drop_table('users')
    op.drop_table('cars')
    # ### end Alembic commands ###
