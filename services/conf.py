from services.implementations.item import ItemServiceImpl
from services.interfaces.item import IItemService

services_dict = {
    IItemService: ItemServiceImpl
}