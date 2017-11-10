""" Add user relationships

Revision ID: 712a54b1a3da
Revises: 0c7fbe465e03
Create Date: 2017-11-08 12:57:07.366249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '712a54b1a3da'
down_revision = '0c7fbe465e03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('constituencies', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'constituencies', 'users', ['user_id'], ['id'])
    op.add_column('counties', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'counties', 'users', ['user_id'], ['id'])
    op.add_column('deputygovernors', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'deputygovernors', 'users', ['user_id'], ['id'])
    op.add_column('governors', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'governors', 'users', ['user_id'], ['id'])
    op.add_column('mcas', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'mcas', 'users', ['user_id'], ['id'])
    op.add_column('parties', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'parties', 'users', ['user_id'], ['id'])
    op.add_column('senators', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'senators', 'users', ['user_id'], ['id'])
    op.add_column('womenreps', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'womenreps', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'womenreps', type_='foreignkey')
    op.drop_column('womenreps', 'user_id')
    op.drop_constraint(None, 'senators', type_='foreignkey')
    op.drop_column('senators', 'user_id')
    op.drop_constraint(None, 'parties', type_='foreignkey')
    op.drop_column('parties', 'user_id')
    op.drop_constraint(None, 'mcas', type_='foreignkey')
    op.drop_column('mcas', 'user_id')
    op.drop_constraint(None, 'governors', type_='foreignkey')
    op.drop_column('governors', 'user_id')
    op.drop_constraint(None, 'deputygovernors', type_='foreignkey')
    op.drop_column('deputygovernors', 'user_id')
    op.drop_constraint(None, 'counties', type_='foreignkey')
    op.drop_column('counties', 'user_id')
    op.drop_constraint(None, 'constituencies', type_='foreignkey')
    op.drop_column('constituencies', 'user_id')
    # ### end Alembic commands ###