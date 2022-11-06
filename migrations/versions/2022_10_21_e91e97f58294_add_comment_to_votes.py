"""add comment to votes

Revision ID: e91e97f58294
Revises: 0abcfa34e032
Create Date: 2022-10-21 17:25:28.958400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e91e97f58294'
down_revision = '0abcfa34e032'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("vote", sa.Column("comment", sa.String(), nullable=True))
    op.add_column("option", sa.Column("comments_enabled", sa.Boolean(), nullable=True))
    op.execute("UPDATE option SET comments_enabled = false")
    op.alter_column('option', 'comments_enabled', nullable=False)


def downgrade():
    op.drop_column("vote", "comment")
    op.drop_column("option", "comments_enabled")
