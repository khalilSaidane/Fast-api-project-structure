from models.models import Item
from models.schemas import ItemCreateSchema
from .crud_base import CRUDBase


class ItemRepository(CRUDBase[Item, ItemCreateSchema, ItemCreateSchema]):
    model: Item = Item
