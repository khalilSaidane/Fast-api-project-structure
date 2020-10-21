from fastapi import APIRouter

from api.routers import item

api_router = APIRouter()

api_router.include_router(item.router, tags=["item"], prefix="/items")
