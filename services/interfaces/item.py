import abc


class IItemService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self):
        pass

    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def remove(self):
        pass
