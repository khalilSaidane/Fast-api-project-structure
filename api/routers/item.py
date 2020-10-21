from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm.exc import UnmappedInstanceError

from api.dependencies.service import get_service
from models.schemas import ItemSchema, ItemCreateSchema
from resources import strings
from services.item import ItemService

router = APIRouter()


@cbv(router)
class ItemRouter:
    item_service: ItemService = Depends(get_service(ItemService))

    @router.post("/", response_model=ItemSchema)
    async def create_item(self, item: ItemCreateSchema):
        return self.item_service.create(item=item)

    @router.get("/{id}", response_model=ItemSchema)
    async def get_item(self, id: int):
        item = self.item_service.get(id=id)
        if not item:
            raise HTTPException(status_code=404, detail=strings.OBJECT_DOES_NOT_EXIST_ERROR)
        return item

    @router.delete('/{id}', response_model=ItemSchema)
    async def remove_item(self, id: int):
        try:
            return self.item_service.remove(id=id)
        except UnmappedInstanceError:
            raise HTTPException(status_code=404, detail=strings.OBJECT_DOES_NOT_EXIST_ERROR)
