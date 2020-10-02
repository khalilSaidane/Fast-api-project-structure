from fastapi import APIRouter, Depends

from api.routers.dependencies.database import get_repository, get_service
from db.repositories.user import UserRepository
from models.schemas import UserOutSchema, UserCreateSchema
from services.authentication import AuthenticationService

router = APIRouter()


@router.post("/login")
async def login(user: UserCreateSchema, service=Depends(get_service(AuthenticationService))):
    user = service.authenticate(email=user.email, password=user.password)
    if user:
        return user.email
    else:
        return {"msg": "error"}