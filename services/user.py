from fastapi import Depends

from core.config import get_settings
from db.errors import EmailAlreadyExists
from db.repositories.item import ItemRepository
from db.repositories.user import UserRepository
from models.schemas import UserCreateSchema
from resources import strings
from services.base import BaseService

settings = get_settings()


class UserService(BaseService):
    # The Order must follow the same order in the constructor
    repositories = [UserRepository, ItemRepository]

    # def __init__(self, user_repository: repositories[0], item_repository: repositories[1]):
    def __init__(self, user_repository: UserRepository, item_repository: ItemRepository):
        self._user_repository = user_repository
        self._item_repository = item_repository

    @property
    def item_repository(self):
        return self._item_repository

    @property
    def user_repository(self):
        return self._user_repository

    def create_user(self, user: UserCreateSchema):
        if self.user_repository.get_user_by_email(email=user.email):
            raise EmailAlreadyExists(strings.EMAIL_ALREADY_REGISTERED_ERROR)
        user.password = user.password + settings.secret_key
        return self.user_repository.create_user(user=user)

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def get_user(self, id: int):
        return self.user_repository.retrieve_user_by_id(id=id)
