from abc import ABCMeta
from src.monKeyData.Items import Item as ItemModule


class Hat(ItemModule.Item):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.item = "hat"


class HatFactory():
    def factory(type, color):
        if type == 0:
            return None
        if type == 1:
            return BackwardsCap()
        if type == 2:
            return Bandana()
        if type == 3:
            return Cap()
        if type == 4:
            return CapBanano()
        if type == 5:
            return CapBebe()
        if type == 6:
            return CapCarlos()
        if type == 7:
            return CapGreenSmug()
        if type == 8:
            return CapKappa()
        if type == 9:
            return CapPepe()
        if type == 10:
            return CapRick()
        if type == 11:
            return CapThonk()
        if type == 12:
            return CapYellowSmug()
        if type == 13:
            return Cowboy()
        if type == 14:
            return Fedora()
        if type == 15:
            return LongHatColorable(color)
        if type == 16:
            return LongHatBananoColorable(color)
        if type == 17:
            return TopHat()
        if type == 18:
            return Viking()
        if type == 19:
            return Warm()
        if type == 20:
            return WarmBanano()
        # ------------Rare Items---------
        if type == 21:
            return Crown()
        if type == 22:
            return Hippie()
        if type == 23:
            return Jester()
        else:
            raise ValueError('Received an unknown Hat type')

    factory = staticmethod(factory)


class BackwardsCap(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'BACKWARDS_CAP'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Backwards Cap"


class Bandana(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'BANDANA'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value':  self.value
        }

    def __str__(self):
        return "Bandana"


class Cap(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'CAP'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Cap"


class CapBanano(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'CAP_BANANO'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Cap Banano"


class CapBebe(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'CAP_BEBE'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Cap Bebe"


class CapCarlos(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'CAP_CARLOS'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Cap Carlos"


class CapGreenSmug(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'CAP_GREEN_SMUG'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Cap Green Smug"


class CapKappa(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'CAP_KAPPA'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Cap Kappa"


class CapPepe(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'CAP_PEPE'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Cap Pepe"


class CapRick(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'CAP_RICK'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Cap Rick"


class CapThonk(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'CAP_THONK'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Cap Thonk"


class CapYellowSmug(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'CAP_YELLOW_SMUG'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Cap Yellow Smug"


class Cowboy(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'COWBOY'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Cowboy"


class Fedora(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'FEDORA'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Fedora"


class LongHatColorable(Hat):
    def __init__(self,color):
        super().__init__()
        self.type = 'LONG_HAT_COLORABLE'
        self.color = color
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'color': self.color,
            'value': self.value
        }

    def __str__(self):
        return "Long Hat"


class LongHatBananoColorable(Hat):
    def __init__(self,color):
        super().__init__()
        self.type = 'LONG_HAT_BANANO_COLORABLE'
        self.color = color
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'color': self.color,
            'value': self.value
        }

    def __str__(self):
        return "Long Hat Banano"


class TopHat(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'TOP_HAT'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Top Hat"


class Viking(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'VIKING'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Viking"


class Warm(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'WARM'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Warm"


class WarmBanano(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'WARM_BANANO'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Warm Banano"


class Crown(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'CROWN'
        self.value = self.Value.Rare.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Crown"


class Hippie(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'HIPPIE'
        self.value = self.Value.Rare.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Hippie"


class Jester(Hat):
    def __init__(self):
        super().__init__()
        self.type = 'JESTER'
        self.value = self.Value.Rare.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Jester"
