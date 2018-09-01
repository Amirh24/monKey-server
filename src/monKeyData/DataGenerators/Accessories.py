from src.monKeyData.Items import Glasses, Tail, Mouth, Misc, Hat, Shoes, ShirtsAndPants


class Accessories:

    def __init__(self,accessories_settings):
        self.glasses = [Glasses.GlassesFactory.factory(accessories_settings.get('glasses'), accessories_settings.get('glasses_color'))]
        self.hat = [Hat.HatFactory.factory(accessories_settings.get('hat'), accessories_settings.get('hat_color'))]
        self.misc = [Misc.MiscFactory.factory(accessories_settings.get('misc'), accessories_settings.get('misc_color'))]
        self.mouth = [Mouth.MouthFactory.factory(accessories_settings.get('mouth'), accessories_settings.get('mouth_color'))]
        self.shirt_and_pants = [ShirtsAndPants.ShirtAndPantsFactory.factory(accessories_settings.get('shirt_and_pants'), accessories_settings.get('shirt_and_pants_color'))]
        self.shoes = [Shoes.ShoesFactory.factory(accessories_settings.get('shoes'), accessories_settings.get('shoes_color'),)]
        self.tail = [Tail.TailFactory.factory(accessories_settings.get('tail'), accessories_settings.get('tail_color'))]

    def serialize(self):
        return {
            'glasses': [glasses.serialize() for glasses in self.glasses if glasses],
            'hat': [hat.serialize() for hat in self.hat if hat],
            'misc': [misc.serialize() for misc in self.misc if misc],
            'mouth': [mouth.serialize() for mouth in self.mouth],
            'shirt_and_pants': [shirt_and_pants.serialize() for shirt_and_pants in self.shirt_and_pants if shirt_and_pants],
            'shoes': [shoes.serialize() for shoes in self.shoes if shoes],
            'tail': [tail.serialize() for tail in self.tail if tail],
        }

    def __iter__(self):
        return iter([self.tail, self.mouth, self.glasses, self.shirt_and_pants, self.hat, self.misc, self.shoes])

    def __str__(self):
        return self.serialize()
