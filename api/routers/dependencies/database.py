from typing import Type

from fastapi import Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.repositories.base import BaseRepository
from db.repositories.user import UserRepository
from services.base import BaseService


def get_repository(repo_type: Type[BaseRepository]):
    def _get_repo(session: Session = Depends(get_db)):
        return repo_type(session)

    return _get_repo


def get_service(repo_type: Type[BaseService]):
    def _get_service(repo: BaseRepository = Depends(get_repository(UserRepository))):
        return repo_type(repo)

    return _get_service
