from db.repositories.base import BaseRepository


class BaseService(object):
    repo = None

    def __init__(self, repository: BaseRepository):
        self._repository = repository

    @property
    def repository(self):
        return self._repository
