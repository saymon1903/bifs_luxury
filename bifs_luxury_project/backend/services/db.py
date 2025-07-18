from sqlmodel import create_engine, SQLModel, Session
import os

DATABASE_URL = os.getenv("DB_URL", "postgresql+asyncpg://bif:lux@localhost/biflux")
engine = create_engine(DATABASE_URL, echo=False, future=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
