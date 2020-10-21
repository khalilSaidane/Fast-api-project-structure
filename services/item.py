from db.repositories.item import ItemRepository
from models.schemas import ItemCreateSchema
from services.base import BaseService


class ItemService(BaseService):
    def __init__(self, item_reo: ItemRepository):
        self.item_repository = item_reo

    def create(self, item: ItemCreateSchema):
        return self.item_repository.create(obj_in=item)

    def get(self, id: int):
        return self.item_repository.get(id=id)

    def remove(self, id: int):
        return self.item_repository.remove(id=id)
