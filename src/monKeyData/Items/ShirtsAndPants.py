from abc import ABCMeta
from src.monKeyData.Items import Item as ItemModule


class ShirtAndPants(ItemModule.Item):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.item = "shirtsandpants"


class ShirtAndPantsFactory():
    def factory(type, color):
        if type == 0:
            return None
        if type == 1:
            return BlueOverall()
        if type == 2:
            return CleanWhiteT()
        if type == 3:
            return Flowery()
        if type == 4:
            return Jeans()
        if type == 5:
            return RedOverall()
        if type == 6:
            return StripesColorable(color)
        else:
            raise ValueError('Received an unknown shirt and pants type')

    factory = staticmethod(factory)


class BlueOverall(ShirtAndPants):
    def __init__(self):
        super().__init__()
        self.type = 'BLUE_OVERALL'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Blue Overall"


class CleanWhiteT(ShirtAndPants):
    def __init__(self):
        super().__init__()
        self.type = 'CLEAN_WHITE_T'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Clean White T"


class Flowery(ShirtAndPants):
    def __init__(self):
        super().__init__()
        self.type = 'FLOWERY'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Flowery"


class Jeans(ShirtAndPants):
    def __init__(self):
        super().__init__()
        self.type = 'JEANS'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Jeans"


class RedOverall(ShirtAndPants):
    def __init__(self, ):
        super().__init__()
        self.type = 'RED_OVERALL'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Red Overall"


class StripesColorable(ShirtAndPants):
    def __init__(self,color):
        super().__init__()
        self.type = 'STRIPES_COLORABLE'
        self.color = color
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'color': self.color,
            'value': self.value
        }

    def __str__(self):
        return "Stripes"
