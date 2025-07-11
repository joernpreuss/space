from sqlalchemy.engine import Engine
from sqlmodel import SQLModel, create_engine


def create_db_and_tables(engine: Engine):
    SQLModel.metadata.create_all(engine)


def get_engine(database_url: str) -> Engine:
    return create_engine(database_url)
