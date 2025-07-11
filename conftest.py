from typing import Generator

import pytest
from sqlalchemy.engine import Engine
from sqlmodel import Session

from backend.db_utils import create_db_and_tables, get_engine
from backend.planet_data import insert_star_system


@pytest.fixture(scope="function")
def engine() -> Engine:
    engine = get_engine("sqlite:///:memory:")
    create_db_and_tables(engine)
    return engine


@pytest.fixture(scope="function")
def session(engine: Engine) -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


@pytest.fixture(scope="function")
def test_data(session: Session):
    result = insert_star_system(session, planets=["Earth", "Mars"])
    return result
