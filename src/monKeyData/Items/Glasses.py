from abc import ABCMeta
from src.monKeyData.Items import Item as ItemModule


class Glasses(ItemModule.Item):
    def __init__(self):
        self.item = "glasses"

    __metaclass__ = ABCMeta


class GlassesFactory():
    def factory(type, color):
        if type == 0:
            return None
        if type == 1:
            return BlackShades()
        if type == 2:
            return BlueAviators()
        if type == 3:
            return BlueTransparent()
        if type == 4:
            return EyePatch()
        if type == 5:
            return GreenAviators()
        if type == 6:
            return GreenTransparent()
        if type == 7:
            return Monocle()
        if type == 8:
            return PinkTransparent()
        if type == 9:
            return YellowAviators()
        else:
            raise ValueError('Received an unknown Glasses type')

    factory = staticmethod(factory)


class BlackShades(Glasses):
    def __init__(self):
        super().__init__()
        self.type = 'BLACK_SHADES'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Black Shades"


class BlueAviators(Glasses):
    def __init__(self):
        super().__init__()
        self.type = 'BLUE_AVIATORS'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Blue Aviators"


class BlueTransparent(Glasses):
    def __init__(self):
        super().__init__()
        self.type = 'BLUE_TRANSPARENT'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Blue Transparent"


class EyePatch(Glasses):
    def __init__(self):
        super().__init__()
        self.type = 'EYE_PATCH'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Eye Patch"


class GreenAviators(Glasses):
    def __init__(self):
        super().__init__()
        self.type = 'BLUE_TRANSPARENT'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Green Aviators"


class Monocle(Glasses):
    def __init__(self):
        super().__init__()
        self.type = 'MONOCLE'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Monocle"


class PinkTransparent(Glasses):
    def __init__(self):
        super().__init__()
        self.type = 'PINK_TRANSPARENT'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Pink Transparent"


class GreenTransparent(Glasses):
    def __init__(self):
        super().__init__()
        self.type = 'GREEN_TRANSPARENT'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Green Transparent"


class YellowAviators(Glasses):
    def __init__(self):
        super().__init__()
        self.type = "YELLOW_AVIATORS"
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Yellow Aviators"
