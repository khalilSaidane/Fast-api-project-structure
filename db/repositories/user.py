from .base import BaseRepository
from models.schemas import UserCreateSchema
from models.models import User
from core.config import get_settings

setting = get_settings()


class UserRepository(BaseRepository):

    def create_user(self, user: UserCreateSchema):
        fake_hashed_password = user.password + setting.secret_key
        user = User(email=user.email, hashed_password=fake_hashed_password)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def retrieve_user_by_id(self, id: int):
        return self.session.query(User).filter(User.id == id).first()

    def update_user(self, id: int, new_user: User):
        user = self.retrieve_user_by_id(id)
        user.email = new_user.email
        user.is_active = new_user.is_active
        user.hashed_password = new_user.hashed_password
        self.session.add(user)
        self.session.commit()

    def delete_user(self, id: int):
        user = self.retrieve_user_by_id(id)
        self.session.delete(user)
        self.session.commit()

    def get_user_by_email_and_password(self, email: str, password: str):
        return self.session.query(User).filter_by(email=email, hashed_password=password).first()
