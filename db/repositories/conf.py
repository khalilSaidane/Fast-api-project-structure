from db.repositories.implementations.item import ItemRepositoryImpl
from db.repositories.interfaces.item import IItemRepository

repository_dict = {
    IItemRepository: ItemRepositoryImpl
}
