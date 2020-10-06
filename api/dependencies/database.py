from typing import Type, List

from fastapi import Depends
from sqlalchemy.orm import Session

from db.database import SessionLocal
from db.repositories.base import BaseRepository
from services.base import BaseService


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_repositories(*repositories):
    def _get_repositories(session: Session = Depends(get_db)):
        """

        :param session:
        :return:  List of instantiated repositories that will be injected in the service
        """
        instantiated_repositories = []
        for repo in repositories:
            instantiated_repositories.append(repo(session))
        return instantiated_repositories

    return _get_repositories


def get_service(service_type: Type[BaseService]):
    def _get_service(repositories: Type[List[BaseRepository]] = Depends(get_repositories(*service_type.repositories))):
        return service_type(*repositories)

    return _get_service
