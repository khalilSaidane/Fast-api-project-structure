from fastapi import Depends
from sqlalchemy.orm import Session
from db.repositories.conf import repository_dict
from api.dependencies.database import get_db


# Every repository depends on a session provided by get_db
def get_repositories(*repositories):
    """

    :param repositories: Non-Keyword Arguments of Repository classes that inherit from BaseRepository.
    :return: A list of instantiated repositories, and pass the session to the constructor.
    """
    repositories_impls = [repository_dict.get(r) for r in repositories]

    def _get_repositories(session: Session = Depends(get_db)):
        instantiated_repositories = []
        for repo in repositories_impls:
            instantiated_repositories.append(repo(session))
        return instantiated_repositories

    return _get_repositories
