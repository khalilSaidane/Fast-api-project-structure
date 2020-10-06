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


# Every repository depends on a session provided by get_db
def get_repositories(*repositories):
    """

    :param repositories: Non-Keyword Arguments of Repository classes that inherit from BaseRepository.
    :return: A list of instantiated repositories, and pass the session to the constructor.
    """

    def _get_repositories(session: Session = Depends(get_db)):
        instantiated_repositories = []
        for repo in repositories:
            instantiated_repositories.append(repo(session))
        return instantiated_repositories

    return _get_repositories


# Every service depends on a list of repositories provided by get_repositories
def get_service(service_type: Type[BaseService]):
    """

    :param service_type: Service Class that inherits from BaseService.
    :return: An instance of the service, and pass the repositories to the constructor.
    """

    def _get_service(repositories: Type[List[BaseRepository]] = Depends(get_repositories(*service_type.repositories))):
        return service_type(*repositories)

    return _get_service
