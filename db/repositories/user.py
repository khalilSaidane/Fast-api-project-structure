from models.schemas import UserCreateSchema, UserUpdateSchema
from models.models import User
from .crud_base import CRUDBase


class UserRepository(CRUDBase[User, UserCreateSchema, UserUpdateSchema]):
    model = User

    def get_user_by_email_and_password(self, email: str, password: str):
        return self.session.query(self.model).filter_by(email=email, hashed_password=password).first()

    def get_user_by_email(self, email: str):
        return self.session.query(self.model).filter(User.email == email).first()
