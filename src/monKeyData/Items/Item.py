from enum import Enum
from abc import ABC, abstractmethod

class Item(ABC):

    @abstractmethod
    def serialize(self):
        pass

    class Value(Enum):
        Basic = 0
        Rare = 1
        Premium = 2
