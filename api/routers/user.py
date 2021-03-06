from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv

from api.dependencies.service import get_service
from db.errors import EmailAlreadyExists
from models.schemas import UserCreateSchema, UserOutSchema
from services.user import UserService
from resources import strings
from api.dependencies.security import CatalogAPIBasePermission


class UserPermission(CatalogAPIBasePermission):
    perms = ["Some-Permission"]


router = APIRouter()


@cbv(router)
class UserRouter:
    service: UserService = Depends(get_service(UserService))
    permission: CatalogAPIBasePermission = Depends(UserPermission())

    @router.post("/", response_model=UserOutSchema)
    async def create_user(self, user: UserCreateSchema):
        try:
            return self.service.create(user=user)
        except EmailAlreadyExists:
            raise HTTPException(status_code=400, detail=strings.EMAIL_ALREADY_REGISTERED_ERROR)

    @router.get("/", response_model=List[UserOutSchema])
    async def get_all_users(self):
        return self.service.get_multi()

    @router.get("/{id}", response_model=UserOutSchema)
    async def read_user(self, id: int):
        user = self.service.get(id=id)
        if not user:
            raise HTTPException(status_code=404, detail=strings.USER_DOES_NOT_EXIST_ERROR)
        return user
