from typing import Type, List
import inspect
from fastapi import Depends

from api.dependencies.repository import get_repositories
from db.repositories.base import BaseRepository
from services.base import BaseService


# Every item_service depends on a list of repositories provided by get_repositories
def get_service(service_type: Type[BaseService]):
    """

    :param service_type: Service Class that inherits from BaseService.
    :return: An instance of the item_service, and pass the repositories to the constructor.
    """
    repository_classes = [
        Repo for Repo in service_type.__init__.__annotations__.values()
        if BaseRepository in inspect.getmro(Repo)
    ]

    def _get_service(repositories: Type[List[BaseRepository]] = Depends(get_repositories(*repository_classes))):
        return service_type(*repositories)

    return _get_service
