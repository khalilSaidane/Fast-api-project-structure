from typing import List

from fastapi import APIRouter, Depends, HTTPException

from api.dependencies.database import get_service
from core.config import get_settings
from db.errors import EmailAlreadyExists
from models.schemas import UserCreateSchema, UserOutSchema
from services.user import UserService
from resources import strings

settings = get_settings()
router = APIRouter()


@router.post("/", response_model=UserOutSchema)
async def create_user(user: UserCreateSchema, service: UserService = Depends(get_service(UserService))):
    try:
        return service.create_user(user=user)
    except EmailAlreadyExists:
        raise HTTPException(status_code=400, detail=strings.EMAIL_ALREADY_REGISTERED_ERROR)


@router.get("/", response_model=List[UserOutSchema])
async def get_all_users(service: UserService = Depends(get_service(UserService))):
    return service.get_all_users()


@router.get("/{id}", response_model=UserOutSchema)
async def read_user(id, service: UserService = Depends(get_service(UserService))):
    user = service.get_user(id=id)
    if user is None:
        raise HTTPException(status_code=404, detail=strings.USER_DOES_NOT_EXIST_ERROR)
    return user
