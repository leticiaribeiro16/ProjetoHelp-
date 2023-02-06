"""empty message

Revision ID: b189ceb9e8f8
Revises: c659c46fa58a
Create Date: 2023-02-06 17:28:46.081675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b189ceb9e8f8'
down_revision = 'c659c46fa58a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('demanda', schema=None) as batch_op:
        batch_op.alter_column('modalidade',
               existing_type=sa.FLOAT(),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('demanda', schema=None) as batch_op:
        batch_op.alter_column('modalidade',
               existing_type=sa.Text(),
               type_=sa.FLOAT(),
               existing_nullable=True)

    # ### end Alembic commands ###