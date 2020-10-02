from fastapi import APIRouter

from api.routers import authentication

api_router = APIRouter()

api_router.include_router(authentication.router, tags=["authentication"], prefix="/users")