from abc import ABCMeta
from src.monKeyData.Items import Item as ItemModule


class Misc(ItemModule.Item):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.item = "misc"


class MiscFactory():
    def factory(type, color):
        if type == 0:
            return None
        if type == 1:
            return BossNecklace()
        if type == 2:
            return Bottle()
        if type == 3:
            return BowTie()
        if type == 4:
            return Camera()
        if type == 5:
            return Club()
        if type == 6:
            return CyanTie()
        if type == 7:
            return Guitar()
        if type == 8:
            return Microphone()
        if type == 9:
            return OneBanana()
        if type == 10:
            return PinkTie()
        if type == 11:
            return TwoBanana()
        if type == 12:
            return WhiteGloves()
        # -------Premium Items-------
        if type == 13:
            return Flamethrower()
        else:
            raise ValueError('Received an unknown Misc type')

    factory = staticmethod(factory)


class BossNecklace(Misc):
    def __init__(self):
        super().__init__()
        self.type = 'BOSS_NECKLACE'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Boss Necklace"


class Bottle(Misc):
    def __init__(self):
        super().__init__()
        self.type = 'BOTTLE'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Bottle"


class BowTie(Misc):
    def __init__(self):
        super().__init__()
        self.type = 'BOW_TIE'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Bow Tie"


class Camera(Misc):
    def __init__(self):
        super().__init__()
        self.type = 'CAMERA'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Camera"


class Club(Misc):
    def __init__(self):
        super().__init__()
        self.type = 'CLUB'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Club"


class CyanTie(Misc):
    def __init__(self):
        super().__init__()
        self.type = 'CYAN_TIE'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Cyan Tie"


class Guitar(Misc):
    def __init__(self):
        super().__init__()
        self.type = 'GUITAR'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Guitar"


class Microphone(Misc):
    def __init__(self):
        super().__init__()
        self.type = 'MICROPHONE'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Microphone"


class OneBanana(Misc):
    def __init__(self):
        super().__init__()
        self.type = 'ONE_BANANA'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "One Banana"


class PinkTie(Misc):
    def __init__(self):
        super().__init__()
        self.type = 'PINK_TIE'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Pink Tie"


class TwoBanana(Misc):
    def __init__(self):
        super().__init__()
        self.type = 'TWO_BANANA'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Two Banana"


class WhiteGloves(Misc):
    def __init__(self):
        super().__init__()
        self.type = 'WHITE_GLOVES'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "White Gloves"


class Flamethrower(Misc):
    def __init__(self):
        super().__init__()
        self.type = 'FLAMETHROWER'
        self.value = self.Value.Premium.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Flamethrower"
