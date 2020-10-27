from db.repositories.implementations.item import ItemRepositoryImpl, ItemRepositoryNewImpl
from db.repositories.interfaces.item import IItemRepository
"""
    In this dic we assign the implementation to the interface
"""
repository_dict = {
    IItemRepository: ItemRepositoryImpl
}
