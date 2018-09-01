from .Accessories import Accessories


class MonKey:
    def __init__(self, monKey_settings):
        self.address = monKey_settings.get('address')
        # self.gender = monKey_settings.get('gender')
        # self.name = monKey_settings.get('name')
        self.status = monKey_settings.get('status')
        self.fur_color = monKey_settings.get('fur_color')
        self.fur_color_in_hex = monKey_settings.get('fur_color_in_hex')
        self.eye_color = monKey_settings.get('eye_color')
        self.eye_color_in_hex = monKey_settings.get('eye_color_in_hex')

        self.accessories = Accessories(monKey_settings.get('accessories'))

    def serialize(self):
        return {
            'address': self.address,
            # 'gender': self.gender,
            # 'name': self.name,
            'status': self.status,
            'fur_color': self.fur_color,
            'fur_color_in_hex': self.fur_color_in_hex,
            'eye_color': self.eye_color,
            'eye_color_in_hex': self.eye_color_in_hex,
            'accessories': self.accessories.serialize()
        }

    def __str__(self):
        return self.serialize()
