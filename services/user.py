from models.schemas import UserCreateSchema
from services.base import BaseService


class UserService(BaseService):

    def create_user(self, user: UserCreateSchema):
        pass
