from models.models import Item
from models.schemas import ItemCreateSchema
from ..crud import CRUDBase
from ..interfaces.item import IItemRepository


class ItemRepositoryImpl(CRUDBase[Item, ItemCreateSchema, ItemCreateSchema], IItemRepository):
    model: Item = Item
