"""empty message

Revision ID: 832c54286843
Revises: 2b570ff957da
Create Date: 2020-07-04 15:55:38.810966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '832c54286843'
down_revision = '2b570ff957da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
