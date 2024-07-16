"""Fix foreign keys and relationships

Revision ID: 6bc1569c4493
Revises: 
Create Date: 2024-07-15 15:15:07.725771

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6bc1569c4493'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('destinations',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=False),
    sa.Column('country', sa.String(length=100), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('attractions', sa.String(length=100), nullable=False),
    sa.Column('bookings_count', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('otp',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('otp', sa.String(length=100), nullable=False),
    sa.Column('expired_time', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('promotions',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('discount_percentage', sa.Float(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_promotions_id'), 'promotions', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('mobile_no', sa.String(length=100), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('is_verified', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('loyalty_programs',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.Column('points', sa.String(length=100), nullable=True),
    sa.Column('tier', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_loyalty_programs_id'), 'loyalty_programs', ['id'], unique=False)
    op.create_table('services',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('service_type', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('available', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_services_name'), 'services', ['name'], unique=False)
    op.create_table('support_tickets',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.Column('subject', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('status', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_support_tickets_id'), 'support_tickets', ['id'], unique=False)
    op.create_table('user_preferences',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.Column('preferred_language', sa.String(length=100), nullable=True),
    sa.Column('preferred_currency', sa.String(length=100), nullable=True),
    sa.Column('email_notifications', sa.Boolean(), nullable=True),
    sa.Column('sms_notifications', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_preferences_id'), 'user_preferences', ['id'], unique=False)
    op.create_table('bookings',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.Column('service_id', sa.String(length=100), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=100), nullable=True),
    sa.Column('total_price', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['service_id'], ['services.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.Column('service_id', sa.String(length=100), nullable=True),
    sa.Column('rating', sa.String(length=100), nullable=True),
    sa.Column('comment', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['service_id'], ['services.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reviews_id'), 'reviews', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reviews_id'), table_name='reviews')
    op.drop_table('reviews')
    op.drop_table('bookings')
    op.drop_index(op.f('ix_user_preferences_id'), table_name='user_preferences')
    op.drop_table('user_preferences')
    op.drop_index(op.f('ix_support_tickets_id'), table_name='support_tickets')
    op.drop_table('support_tickets')
    op.drop_index(op.f('ix_services_name'), table_name='services')
    op.drop_table('services')
    op.drop_index(op.f('ix_loyalty_programs_id'), table_name='loyalty_programs')
    op.drop_table('loyalty_programs')
    op.drop_table('users')
    op.drop_index(op.f('ix_promotions_id'), table_name='promotions')
    op.drop_table('promotions')
    op.drop_table('otp')
    op.drop_table('destinations')
    # ### end Alembic commands ###