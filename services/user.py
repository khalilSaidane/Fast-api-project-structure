from fastapi import Depends

from core.config import get_settings
from db.errors import EmailAlreadyExists
from db.repositories.user import UserRepository
from models.schemas import UserCreateSchema
from resources import strings
from services.base import BaseService

settings = get_settings()


class UserService(BaseService):
    repo_class = UserRepository

    def create_user(self, user: UserCreateSchema):
        if self.repository.get_user_by_email(email=user.email):
            raise EmailAlreadyExists(strings.EMAIL_ALREADY_REGISTERED_ERROR)
        user.password = user.password + settings.secret_key
        return self.repository.create_user(user=user)

    def get_all_users(self):
        return self.repository.get_all_users()

    def get_user(self, id: int):
        return self.repository.retrieve_user_by_id(id=id)
