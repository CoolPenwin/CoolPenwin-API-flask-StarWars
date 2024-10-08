"""empty message

Revision ID: 543569391695
Revises: 0ea5a20ae14f
Create Date: 2024-09-13 13:27:09.275005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '543569391695'
down_revision = '0ea5a20ae14f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('films_characters',
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['film_id'], ['films.id'], ),
    sa.PrimaryKeyConstraint('film_id', 'character_id')
    )
    op.create_table('films_planets',
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['film_id'], ['films.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.PrimaryKeyConstraint('film_id', 'planet_id')
    )
    op.create_table('films_species',
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('species_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['film_id'], ['films.id'], ),
    sa.ForeignKeyConstraint(['species_id'], ['species.id'], ),
    sa.PrimaryKeyConstraint('film_id', 'species_id')
    )
    op.create_table('films_starships',
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('starship_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['film_id'], ['films.id'], ),
    sa.ForeignKeyConstraint(['starship_id'], ['starships.id'], ),
    sa.PrimaryKeyConstraint('film_id', 'starship_id')
    )
    op.create_table('liked',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('item_type', sa.String(length=50), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('starship_id', sa.Integer(), nullable=True),
    sa.Column('species_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['species_id'], ['species.id'], ),
    sa.ForeignKeyConstraint(['starship_id'], ['starships.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'item_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('liked')
    op.drop_table('films_starships')
    op.drop_table('films_species')
    op.drop_table('films_planets')
    op.drop_table('films_characters')
    # ### end Alembic commands ###
