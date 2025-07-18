from logging.config import fileConfig
from sqlmodel import SQLModel
from alembic import context
from services.db import engine
from api.models import *  # noqa

config = context.config
fileConfig(config.config_file_name)
target_metadata = SQLModel.metadata

def run_migrations_online():
    with engine.begin() as conn:
        context.configure(connection=conn, target_metadata=target_metadata)
        context.run_migrations()

run_migrations_online()
