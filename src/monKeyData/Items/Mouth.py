from abc import ABCMeta
from src.monKeyData.Items import Item as ItemModule


class Mouth(ItemModule.Item):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.item = "mouth"


class MouthFactory():
    def factory(type, color):
        if type == 0:
            return BigTeethSmile()
        if type == 1:
            return Cigar()
        if type == 2:
            return ClosedMouthSmile()
        if type == 3:
            return Confused()
        if type == 4:
            return Meh()
        if type == 5:
            return Pipe()
        if type == 6:
            return ToungeOut()
        # -----Rare Items-----
        if type == 7:
            return Joint()
        else:
            raise ValueError('Received an unknown Mouth type')

    factory = staticmethod(factory)


class BigTeethSmile(Mouth):
    def __init__(self):
        super().__init__()
        self.type = 'BIG_TEETH_SMILE'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Big Teeth Smile"


class Cigar(Mouth):
    def __init__(self):
        super().__init__()
        self.type = 'CIGAR'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Cigar"


class ClosedMouthSmile(Mouth):
    def __init__(self):
        super().__init__()

        self.type = 'CLOSED_MOUTH_SMILE'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Closed Mouth Smile"


class Confused(Mouth):
    def __init__(self):
        super().__init__()
        self.type = 'CONFUSED'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Confused"


class Meh(Mouth):
    def __init__(self):
        super().__init__()
        self.type = 'MEH'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Meh"


class Pipe(Mouth):
    def __init__(self):
        super().__init__()
        self.type = 'PIPE'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Pipe"


class ToungeOut(Mouth):
    def __init__(self):
        super().__init__()
        self.type = 'TONGUE_OUT'
        self.value = self.Value.Basic.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Tounge Out"


class Joint(Mouth):
    def __init__(self):
        super().__init__()
        self.type = 'JOINT'
        self.value = self.Value.Rare.name

    def serialize(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def __str__(self):
        return "Joint"
