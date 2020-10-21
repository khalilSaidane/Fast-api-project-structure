from db.repositories.interfaces.item import IItemRepository
from models.schemas import ItemCreateSchema
from services.base import BaseService
from services.interfaces.item import IItemService


class ItemServiceImpl(BaseService, IItemService):
    def __init__(self, item_reo: IItemRepository):
        self.item_repository = item_reo

    def create(self, item: ItemCreateSchema):
        return self.item_repository.create(obj_in=item)

    def get(self, id: int):
        return self.item_repository.get(id=id)

    def remove(self, id: int):
        return self.item_repository.remove(id=id)
