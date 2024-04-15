"""add language to posts

Revision ID: 887646264aa2
Revises: 368ee1d2d48c
Create Date: 2024-04-07 20:40:06.656207

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "887646264aa2"
down_revision = "5b73cb519c4a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("post", schema=None) as batch_op:
        batch_op.add_column(sa.Column("language", sa.String(length=5), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("post", schema=None) as batch_op:
        batch_op.drop_column("language")

    # ### end Alembic commands ###
