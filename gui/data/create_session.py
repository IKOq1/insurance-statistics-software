from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session


def create_session() -> Session:
    engine = create_engine("sqlite+pysqlite:///MainDB.db", echo=True)

    s = Session(engine)
    return s