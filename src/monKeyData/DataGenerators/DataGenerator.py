class DataGenerator:
    def __init__(self):
        self.alphabet = '13456789abcdefghijkmnopqrstuwxyz'

    # Banano/NANO Addresses are made of base 32 numbers (0-9 and a - z not including 0,2,l,v)
    def base32decode(self, base32_number):
        base10_number = 0
        for idx, ch in enumerate(reversed(base32_number)):
            base10_number += pow(32, idx) * self.alphabet.find(ch)
        return base10_number

    def get_RGB_tuple_from_base32_number(self, address_substring):

        base10_number = self.base32decode(address_substring)
        # Make number be in the range of 0 - 256^3 = 16,777,216 for an RGB number
        reduced_number = base10_number % pow(256, 3)
        r = reduced_number % 256
        g = ((reduced_number - r) / 256) % 256
        b = (reduced_number - r - 256 * g) / pow(256, 2)
        # Return (Red,Green,Blue,Alpha) tuple

        return int(r), int(g), int(b)
