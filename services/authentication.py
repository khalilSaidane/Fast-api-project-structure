from core.config import get_settings
from services.base import BaseService

settings = get_settings()


class AuthenticationService(BaseService):
    def authenticate(self, email: str, password: str):
        user = self.repository.get_user_by_email_and_password(email=email, password=password)
        return user
