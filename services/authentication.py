from db.repositories.user import UserRepository
from services.base import BaseService


class AuthenticationService(BaseService):
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    @property
    def user_repository(self):
        return self._user_repository

    def authenticate(self, email: str, password: str):
        user = self.user_repository.get_user_by_email_and_password(email=email, password=password)
        return user
