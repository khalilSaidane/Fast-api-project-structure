from fastapi import APIRouter, Depends

from api.dependencies.database import get_service
from models.schemas import UserCreateSchema
from services.authentication import AuthenticationService

router = APIRouter()


@router.post("/login")
async def login(user: UserCreateSchema, service=Depends(get_service(AuthenticationService))):
    user = service.authenticate(email=user.email, password=user.password)
    if user:
        return user.email
    else:
        return {"msg": "error"}
