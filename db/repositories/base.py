from fastapi import Depends
from sqlalchemy.orm import Session

from db.database import get_db


class BaseRepository:
    def __init__(self, session: Session):
        self._session = session

    @property
    def session(self):
        return self._session
