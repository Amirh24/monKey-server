from abc import ABCMeta
from src.monKeyData.Items import Item as ItemModule


class Tail(ItemModule.Item):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.item = "tail"


class TailFactory():
    def factory(type, color):
        if type == 0:
            return None
        if type == 1:
            return TailColorable(color)
        else:
            raise ValueError('Received an unknown Tail type')

    factory = staticmethod(factory)


class TailColorable(Tail):
    def __init__(self, color):
        super().__init__()
        self.type = 'TAIL_COLORABLE'
        self.color = color
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'color': self.color,
            'value': self.value
        }

    def __str__(self):
        return "Tail"
