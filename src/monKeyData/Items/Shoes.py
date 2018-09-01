from abc import ABCMeta
from src.monKeyData.Items import Item as ItemModule


class Shoes(ItemModule.Item):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.item = "shoes"


class ShoesFactory():
    def factory(type, color):
        if type == 0:
            return None
        if type == 1:
            return BlueShoes()
        if type == 2:
            return CleanWhiteShoes()
        if type == 3:
            return GraySlippers()
        if type == 4:
            return GreenShoes()
        if type == 5:
            return RedShoes()
        if type == 6:
            return SocksColorable(color)
        else:
            raise ValueError('Received an unknown Shoes type')

    factory = staticmethod(factory)


class BlueShoes(Shoes):
    def __init__(self):
        super().__init__()
        self.type = 'BLUE_SHOES'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Blue Shoes"


class CleanWhiteShoes(Shoes):
    def __init__(self):
        super().__init__()
        self.type = 'CLEAN_WHITE_SHOES'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Clean White Shoes"


class GraySlippers(Shoes):
    def __init__(self):
        super().__init__()
        self.type = 'GRAY_SLIPPERS'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Gray Slippers"


class GreenShoes(Shoes):
    def __init__(self):
        super().__init__()
        self.type = 'GREEN_SHOES'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Green Shoes"


class RedShoes(Shoes):
    def __init__(self):
        super().__init__()
        self.type = 'RED_SHOES'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Red Shoes"


class SocksColorable(Shoes):
    def __init__(self,color):
        super().__init__()
        self.type = 'SOCKS_COLORABLE'
        self.color = color
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'color': self.color,
            'value': self.value
        }

    def __str__(self):
        return "Socks"