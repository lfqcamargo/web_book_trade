"""Add notification users

Revision ID: 827a8c6b4689
Revises: f2470e6d9d67
Create Date: 2024-05-30 10:17:20.898129

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '827a8c6b4689'
down_revision: Union[str, None] = 'f2470e6d9d67'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('addresses', 'public',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.add_column('users', sa.Column('whatsapp', sa.String(length=14), nullable=True))
    op.add_column('users', sa.Column('notification_email', sa.Boolean(), nullable=False))
    op.add_column('users', sa.Column('notification_whats', sa.Boolean(), nullable=False))
    op.create_unique_constraint(None, 'users', ['whatsapp'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'notification_whats')
    op.drop_column('users', 'notification_email')
    op.drop_column('users', 'whatsapp')
    op.alter_column('addresses', 'public',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
