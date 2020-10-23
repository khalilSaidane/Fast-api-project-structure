from models.models import Item
from models.schemas import ItemCreateSchema
from ..crud import CRUDBase
from ..interfaces.item import IItemRepository
import time


class ItemRepositoryImpl(CRUDBase[Item, ItemCreateSchema, ItemCreateSchema], IItemRepository):
    model: Item = Item

    def get(self, id: int):
        time.sleep(2)
        return super(ItemRepositoryImpl, self).get(id=id)


class ItemRepositoryNewImpl(CRUDBase[Item, ItemCreateSchema, ItemCreateSchema], IItemRepository):
    model: Item = Item
