from typing import Type

from fastapi import Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.repositories.base import BaseRepository
from services.base import BaseService


def get_repository(**repos):
    print(repos)

    def _get_repo(session: Session = Depends(get_db)):
        """

        :param session:
        :return: dictionary, key is the name of the repository param passed to the service example "user_repository"
        value an instance of that repository with the session passed as a parameter example UserRepository(session)
        """
        repositories = {}
        for key, val in repos.items():
            repositories.update({key: val(session)})
        return repositories

    return _get_repo


def get_service(service_type: Type[BaseService]):

    def _get_service(repositories=Depends(get_repository(**service_type.repositories))):
        return service_type(**repositories)

    return _get_service
