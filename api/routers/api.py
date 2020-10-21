from fastapi import APIRouter

from api.routers import authentication
from api.routers import user
from api.routers import item

api_router = APIRouter()

api_router.include_router(authentication.router, tags=["authentication"], prefix="/auth")
api_router.include_router(user.router, tags=["user"], prefix="/users")
api_router.include_router(item.router, tags=["item"], prefix="/items")
