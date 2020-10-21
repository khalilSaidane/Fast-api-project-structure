from models.models import Item
from models.schemas import ItemCreateSchema
from ..crud import CRUDBase
from ..interfaces.item import IItemRepository


class ItemRepositoryImpl(CRUDBase[Item, ItemCreateSchema, ItemCreateSchema], IItemRepository):
    model: Item = Item


class ItemRepositoryNewImpl(CRUDBase[Item, ItemCreateSchema, ItemCreateSchema], IItemRepository):
    model: Item = Item

    def get(self, id: int):
        return {
            "title": "item",
            "description": "New Item..",
            "id": 2,
        }
