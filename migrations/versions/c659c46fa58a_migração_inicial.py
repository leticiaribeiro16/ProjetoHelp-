"""Migração inicial

Revision ID: c659c46fa58a
Revises: 
Create Date: 2023-02-06 17:06:45.958366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c659c46fa58a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('edital',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=100), nullable=True),
    sa.Column('paragrafo', sa.String(length=100), nullable=True),
    sa.Column('link', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('matricula', sa.String(length=100), nullable=True),
    sa.Column('senha', sa.String(length=100), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.Column('professor', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('aprovacao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_usuario', sa.Integer(), nullable=True),
    sa.Column('nota', sa.Float(), nullable=True),
    sa.Column('aprovacao', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuario.matricula'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('demanda',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('materia', sa.String(length=100), nullable=True),
    sa.Column('observacoes', sa.Text(), nullable=True),
    sa.Column('requisitos', sa.Text(), nullable=True),
    sa.Column('conteudo', sa.Text(), nullable=True),
    sa.Column('orientadores', sa.Text(), nullable=True),
    sa.Column('id_edital', sa.Integer(), nullable=True),
    sa.Column('modalidade', sa.Float(), nullable=True),
    sa.Column('validacao', sa.Boolean(), nullable=True),
    sa.Column('vagas_matutino', sa.Float(), nullable=True),
    sa.Column('vagas_vespertino', sa.Float(), nullable=True),
    sa.Column('vagas_noturno', sa.Float(), nullable=True),
    sa.Column('vagas_flexivel', sa.Float(), nullable=True),
    sa.Column('bolsas', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['id_edital'], ['edital.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inscricao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_usuario', sa.Integer(), nullable=True),
    sa.Column('id_edital', sa.Integer(), nullable=True),
    sa.Column('turno', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['id_edital'], ['edital.id'], ),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuario.matricula'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inscricao')
    op.drop_table('demanda')
    op.drop_table('aprovacao')
    op.drop_table('usuario')
    op.drop_table('edital')
    # ### end Alembic commands ###
