import abc


class IItemRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def get_multi(self):
        pass

    @abc.abstractmethod
    def create(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def remove(self, id: int):
        pass
