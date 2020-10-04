from fastapi import APIRouter, Depends

from api.routers.dependencies.database import get_repository, get_service
from db.repositories.user import UserRepository
from models.models import User
from models.schemas import UserOutSchema, UserCreateSchema
from services.authentication import AuthenticationService
from services.user import UserService
from core.config import get_settings
settings = get_settings()

router = APIRouter()


@router.post("/login")
async def login(user: UserCreateSchema, service=Depends(get_service(AuthenticationService))):
    user = service.authenticate(email=user.email, password=user.password)
    if user:
        return user.email
    else:
        return {"msg": "error"}

# @router.post("/")
# async def create_user(user: UserCreateSchema, service=Depends(get_service(UserService, UserRepository))):
#     user_db = User(email=user.email, hashed_password=user.password+settings.secret_key)
#



