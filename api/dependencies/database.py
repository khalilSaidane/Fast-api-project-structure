from typing import Type, List

from fastapi import Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.repositories.base import BaseRepository
from services.base import BaseService


def get_repository(*repos):
    print("*"*50, repos)

    def _get_repo(session: Session = Depends(get_db)):
        """

        :param session:
        :return: List of instantiated repositories that a service defines as a constant
        and then uses in the same order in its constructor
        """
        instantiated_repositories = []
        for repo in repos:
            instantiated_repositories.append(repo(session))
        return instantiated_repositories

    return _get_repo


def get_service(service_type: Type[BaseService]):
    def _get_service(repositories: Type[List[BaseRepository]] = Depends(get_repository(*service_type.repositories))):
        print("-" * 50, repositories)
        return service_type(*repositories)

    return _get_service
