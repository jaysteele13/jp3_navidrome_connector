import sqlite3


# Bring in helper
from .db_helpers.connect import connect_to_db


from typing import Annotated
from sqlmodel import Session

from fastapi import Depends


# Initialise the Session Dependency for whole app
engine = connect_to_db()


def get_session():
    with Session(engine) as session:
        yield session


# Have SessionDep at the top - DI
SessionDep = Annotated[Session, Depends(get_session)]	 
