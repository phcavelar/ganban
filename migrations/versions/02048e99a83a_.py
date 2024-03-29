"""empty message

Revision ID: 02048e99a83a
Revises: d71fef60c213
Create Date: 2019-08-17 10:47:54.022808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02048e99a83a'
down_revision = 'd71fef60c213'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
