import sys
from enum import IntEnum
from .DataGenerator import DataGenerator


class AccessoriesDataGenerator(DataGenerator):

    class GlassesType(IntEnum):
        NONE = 0
        BLACK_SHADES = 1
        BLUE_AVIATORS = 2
        BLUE_TRANSPARENT = 3
        EYE_PATCH = 4
        GREEN_AVIATORS = 5
        GREEN_TRANSPARENT = 6
        MONOCLE = 7
        PINK_TRANSPARENT = 8
        YELLOW_AVIATORS = 9

    class HatType(IntEnum):
        NONE = 0
        BACKWARDS_CAP = 1
        BANDANA = 2
        CAP = 3
        CAP_BANANO = 4
        CAP_BEBE = 5
        CAP_CARLOS = 6
        CAP_GREEN_SMUG = 7
        CAP_KAPPA = 8
        CAP_PEPE = 9
        CAP_RICK = 10
        CAP_THONK = 11
        CAP_YELLOW_SMUG = 12
        COWBOY = 13
        FEDORA = 14
        LONG_HAT_BANANO_COLORABLE = 15
        LONG_HAT_COLORABLE = 16
        TOP_HAT = 17
        VIKING = 18
        WARM = 19
        WARM_BANANO = 20
        # Rare Items
        CROWN = 21
        HIPPIE = 22
        JESTER = 23

    class MisCType(IntEnum):
        NONE = 0
        BOSS_NECKLACE = 1
        BOTTLE = 2
        BOW_TIE = 3
        CAMERA = 4
        CLUB = 5
        CYAN_TIE = 6
        GUITAR = 7
        MICROPHONE = 8
        ONE_BANANA = 9
        PINK_TIE = 10
        TWO_BANANA = 11
        WHITE_GLOVES = 12
    #     Premium Items
        FLAMETHROWER = 13

    class MouthType(IntEnum):
        BIG_TEETH_SMILE = 0
        CIGAR = 1
        CLOSED_MOUTH_SMILE = 2
        CONFUSED = 3
        MEH = 4
        PIPE = 5
        TONGUE_OUT = 6
    #     Rare Items
        JOINT = 7

    class ShirtAndPantsType(IntEnum):
        NONE = 0
        BLUE_OVERALL = 1
        CLEAN_WHITE_T = 2
        FLOWERY = 3
        JEANS = 4
        RED_OVERALL = 5
        STRIPES_COLORABLE = 6

    class ShoesType(IntEnum):
        NONE = 0
        BLUE_SHOES = 1
        CLEAN_WHITE_SHOES = 2
        GRAY_SLIPPERS = 3
        GREEN_SHOES = 4
        RED_SHOES = 5
        SOCKS_COLORABLE = 6

    class TailType(IntEnum):
        NONE = 0
        TAIL_COLORABLE = 1


    def __init__(self):
        super().__init__()
        self.basic_glasses_options = {
            '11': self.GlassesType.BLACK_SHADES,
            '12': self.GlassesType.BLUE_AVIATORS,
            '13': self.GlassesType.GREEN_AVIATORS,
            '14': self.GlassesType.YELLOW_AVIATORS,
            '15': self.GlassesType.MONOCLE,
            '16': self.GlassesType.BLUE_TRANSPARENT,
            '17': self.GlassesType.GREEN_TRANSPARENT,
            '18': self.GlassesType.PINK_TRANSPARENT,
            '19': self.GlassesType.EYE_PATCH
        }

        self.basic_hat_options = {
            '2': self.HatType.BACKWARDS_CAP,
            '4': self.HatType.BANDANA,
            '5': self.HatType.CAP,
            '6': self.HatType.CAP_BANANO,
            '7': self.HatType.CAP_BEBE,
            '8': self.HatType.CAP_CARLOS,
            '9': self.HatType.CAP_GREEN_SMUG,
            '10': self.HatType.CAP_KAPPA,
            '12': self.HatType.CAP_PEPE,
            '14': self.HatType.CAP_RICK,
            '15': self.HatType.CAP_THONK,
            '16': self.HatType.CAP_YELLOW_SMUG,
            '17': self.HatType.COWBOY,
            '18': self.HatType.FEDORA,
            '20': self.HatType.LONG_HAT_BANANO_COLORABLE,
            '21': self.HatType.LONG_HAT_COLORABLE,
            '22': self.HatType.VIKING,
            '23': self.HatType.WARM,
            '24': self.HatType.WARM_BANANO,
            '26': self.HatType.TOP_HAT,
            '30': self.HatType.LONG_HAT_BANANO_COLORABLE,
            '31': self.HatType.LONG_HAT_COLORABLE
        }

        self.basic_misc_options = {
            '17': self.MisCType.BOSS_NECKLACE,
            '18': self.MisCType.BOTTLE,
            '19': self.MisCType.BOW_TIE,
            '20': self.MisCType.CAMERA,
            '21': self.MisCType.CLUB,
            '22': self.MisCType.CYAN_TIE,
            '23': self.MisCType.GUITAR,
            '24': self.MisCType.MICROPHONE,
            '25': self.MisCType.ONE_BANANA,
            '26': self.MisCType.PINK_TIE,
            '27': self.MisCType.TWO_BANANA,
            '28': self.MisCType.WHITE_GLOVES
        }

        self.basic_shirts_and_pants_options = {
            '1': self.ShirtAndPantsType.BLUE_OVERALL,
            '6': self.ShirtAndPantsType.CLEAN_WHITE_T,
            '13': self.ShirtAndPantsType.JEANS,
            '22': self.ShirtAndPantsType.FLOWERY,
            '19': self.ShirtAndPantsType.RED_OVERALL,
            '8':  self.ShirtAndPantsType.STRIPES_COLORABLE,
            '15': self.ShirtAndPantsType.STRIPES_COLORABLE,
            '24': self.ShirtAndPantsType.STRIPES_COLORABLE,
            '28': self.ShirtAndPantsType.STRIPES_COLORABLE
        }
        self.basic_shoes_options = {
            '3': self.ShoesType.BLUE_SHOES,
            '7': self.ShoesType.CLEAN_WHITE_SHOES,
            '14': self.ShoesType.GRAY_SLIPPERS,
            '18': self.ShoesType.GREEN_SHOES,
            '21': self.ShoesType.RED_SHOES,
            '9': self.ShoesType.SOCKS_COLORABLE,
            '25': self.ShoesType.SOCKS_COLORABLE,
            '27': self.ShoesType.SOCKS_COLORABLE,
            '29': self.ShoesType.SOCKS_COLORABLE
        }
        self.basic_tail_options = {
            '5': self.TailType.TAIL_COLORABLE,
            '6': self.TailType.TAIL_COLORABLE,
            '7': self.TailType.TAIL_COLORABLE,
            '8': self.TailType.TAIL_COLORABLE,
            '9': self.TailType.TAIL_COLORABLE,
            '10': self.TailType.TAIL_COLORABLE,
            '25': self.TailType.TAIL_COLORABLE,
            '26': self.TailType.TAIL_COLORABLE,
            '27': self.TailType.TAIL_COLORABLE,
            '28': self.TailType.TAIL_COLORABLE,
            '29': self.TailType.TAIL_COLORABLE,
            '30': self.TailType.TAIL_COLORABLE
        }
        self.item_index_to_dictionary = {
            1: self.basic_glasses_options,
            2: self.basic_hat_options,
            3: self.basic_misc_options,
            4: self.basic_shirts_and_pants_options,
            5: self.basic_shoes_options,
            6: self.basic_tail_options
        }
        self.accessories_colors = [
                                (139,0,0), #dark red
                                (165,42,42), #brown
                                (178,34,34), #firebrick
                                (255,0,0), #red
                                (255,127,80), #coral
                                (205,92,92), #indian red
                                (240,128,128), #light coral
                                (233,150,122), #dark salmon
                                (250,128,114), #salmon
                                (255,160,122), #light salmon
                                (255,69,0), #orange red
                                (255,140,0), #dark orange
                                (255,165,0), #orange
                                (255,215,0), #gold
                                (184,134,11), #dark golden rod
                                (218,165,32), #golden rod
                                (238,232,170), #pale golden rod
                                (189,183,107), #dark khaki
                                (240,230,140), #khaki
                                (128,128,0), #olive
                                (255,255,0), #yellow
                                (154,205,50), #yellow green
                                (85,107,47), #dark olive green
                                (107,142,35), #olive drab
                                (124,252,0), #lawn green
                                (127,255,0), #chart reuse
                                (173,255,47), #green yellow
                                (0,100,0), #dark green
                                (0, 128, 0), #green
                                (0,255,0), #lime
                                (50,205,50), #lime green
                                (144,238,144), #light green
                                (152,251,152), #pale green
                                (143,188,143), #dark sea green
                                (0,250,154), #medium spring green
                                (0,255,127), #spring green
                                (46,139,87), #sea green
                                (102,205,170), #medium aqua marine
                                (60,179,113), #medium sea green
                                (32,178,170), #light sea green
                                (47,79,79), #dark slate gray
                                (0,128,128), #teal
                                (0,139,139), #dark cyan
                                (0,255,255), #cyan
                                (224,255,255), #light cyan
                                (0,206,209), #dark turquoise
                                (64,224,208), #turquoise
                                (72,209,204), #medium turquoise
                                (175,238,238,), #pale turquoise
                                (127,255,212), #aqua marine
                                (176,224,230), #powder blue
                                (95,158,160), #cadet blue
                                (70,130,180), #steel blue
                                (100,149,237), #corn flower blue
                                (0,191,255), #deep sky blue
                                (30,144,255), #dodger blue
                                (173,216,230), #light blue
                                (135,206,235), #sky blue
                                (25,25,112), #midnight blue
                                (0,0,139), #dark blue
                                (0,0,205), #medium blue
                                (0,0,255), #blue
                                (65,105,225), #royal blue
                                (138,43,226), #blue violet
                                (75,0,130), #indigo
                                (72,61,139), #dark slate blue
                                (106,90,205), #slate blue
                                (123,104,238), #medium slate blue
                                (147,112,219), #medium purple
                                (139,0,139), #dark magenta
                                (148,0,211), #dark violet
                                (153,50,204), #dark orchid
                                (186,85,211), #medium orchid
                                (128,0,128), #purple
                                (216,191,216), #thistle
                                (238,130,238), #violet
                                (255,0,255), #magenta / fuchsia
                                (218,112,214), #orchid
                                (199,21,133), #medium violet red
                                (219,112,147), #pale violet red
                                (255,20,147), #deep pink
                                (255,105,180), #hot pink
                                (255,192,203), #pink
                                (250,235,215), #antique white
                                (245,245,220), #beige
                                (255,228,196), #bisque
                                (255,235,205), #blanched almond
                                (245,222,179), #wheat
                                (255,250,205), #lemon chiffon
                                (250,250,210), #light golden rod yellow
                                (255,255,224), #light yellow
                                (139,69,19), #saddle brown
                                (160,82,45), #sienna
                                (210,105,30), #chocolate
                                (205,133,63), #peru
                                (244,164,96), #sandy brown
                                (222,184,135), #burly wood
                                (210,180,140), #tan
                                (188,143,143), #rosy brown
                                (255,222,173), #navajo white
                                (255,218,185), #peach puff
                                (255,228,225), #misty rose
                                (255,240,245), #lavender blush
                                (250,240,230), #linen
                                (253,245,230), #old lace
                                (255,239,213), #papaya whip
                                (255,245,238), #sea shell
                                (245,255,250), #mint cream
                                (112,128,144), #slate gray
                                (119,136,153), #light slate gray
                                (176,196,222), #light steel blue
                                (230,230,250), #lavender
                                (255,250,240), #floral white
                                (240,248,255), #alice blue
                                (248,248,255), #ghost white
                                (240,255,240), #honeydew
                                (255,255,240), #ivory
                                (240,255,255), #azure
                                (255,250,250), #snow
                                (0,0,0), #black
                                (105,105,105), #dim gray / dim grey
                                (128,128,128), #gray / grey
                                (169,169,169), #dark gray / dark grey
                                (192,192,192), #silver
                                (211,211,211), #light gray / light grey
                                (220,220,220), #gainsboro
                                (245,245,245), #white smoke
                                (255,255,255), #white
                                ]

    def create_item_from_type(self,item_type_index,base_32_digit):
            item_type_dictionary = self.item_index_to_dictionary[item_type_index]
            number = str(self.alphabet.find(base_32_digit))
            # All items have a NONE option which is always 0
            item_type = 0
            try:
                if number in item_type_dictionary:
                    item_type = int(item_type_dictionary[number])
            except:
                e = sys.exc_info()[0]
                print(e)
            finally:
                return item_type

    def create_mouth_type(self, base_32_digit, add_joint):
        number = self.alphabet.find(base_32_digit)
        mouth_type = int(self.MouthType.BIG_TEETH_SMILE)
        try:
            if add_joint and number == 0:
                mouth_type = int(self.MouthType.JOINT)
            elif number >= 8 and number <= 11:
                mouth_type = int(self.MouthType.TONGUE_OUT)
            elif number >= 12 and number <= 18:
                mouth_type = int(self.MouthType.CLOSED_MOUTH_SMILE)
            elif number >= 19 and number <= 24:
                mouth_type = int(self.MouthType.CONFUSED)
            elif number >= 25 and number <= 29:
               mouth_type = int(self.MouthType.MEH)
            elif number == 30:
               mouth_type = int(self.MouthType.PIPE)
            elif number == 31:
               mouth_type = int(self.MouthType.CIGAR)
        except:
            e = sys.exc_info()[0]
            print(e)
        finally:
            return mouth_type

    def create_accessory_color_in_hex(self,two_base_32_digits):
        # There are only 128 colors and 32 * 32 = 1024 options
        base10_number = self.base32decode(two_base_32_digits) % 128
        rgb_color = self.accessories_colors[base10_number]
        return '#%02x%02x%02x' % rgb_color

    def generate_accessories_data_from_address(self, banano_address):

        # Check for rare items
        add_crown = self.alphabet.find(banano_address[-40]) == 15
        add_hippie = self.alphabet.find(banano_address[-41]) == 2
        add_jester = self.alphabet.find(banano_address[-42]) == 20
        add_joint = self.alphabet.find(banano_address[-43]) == 9
        add_flamethrower = self.alphabet.find(banano_address[-44]) == 24 and self.alphabet.find(banano_address[-45]) < 10

        # Add rare items into dictionaries
        if add_crown:
            self.basic_hat_options['1'] = self.HatType.CROWN
        if add_hippie:
            self.basic_hat_options['27'] = self.HatType.HIPPIE
        if add_jester:
            self.basic_hat_options['28'] = self.HatType.JESTER
        # Check for premium items
        if add_flamethrower:
            self.basic_misc_options['5'] = self.MisCType.FLAMETHROWER

        glasses_type = banano_address[-19]
        glasses_color = banano_address[-21:-19]
        tail_type = banano_address[-22]
        tail_color = banano_address[-24:-22]
        mouth_type = banano_address[-25]
        mouth_color = banano_address[-27:-25]
        misc_type = banano_address[-28]
        misc_color = banano_address[-30:-28]
        hat_type = banano_address[-31]
        hat_color = banano_address[-33:-31]
        shirt_and_pants_type = banano_address[- 34]
        shirt_and_pants_color = banano_address[-36:-34]
        shoes_type = banano_address[- 37]
        shoes_color = banano_address[-39: -37]

        accessories_data = {
            # (0,0,0,255) is being used right now because we still don't have colorable items in this type of accessory
            'glasses':  self.create_item_from_type(1, glasses_type),
        #    'glasses_color': self.create_accessory_color(glasses_color),
            'glasses_color': (0,0,0,255),
            'hat': self.create_item_from_type(2, hat_type),
            'hat_color': self.create_accessory_color_in_hex(hat_color),
            'misc': self.create_item_from_type(3, misc_type),
           # 'misc_color': self.create_accessory_color(misc_color),
            'misc_color': (0,0,0,255),
            'mouth': self.create_mouth_type(mouth_type, add_joint),
          #  'mouth_color': self.create_accessory_color(mouth_color),
            'mouth_color': (0, 0, 0, 255),
            'shirt_and_pants': self.create_item_from_type(4, shirt_and_pants_type),
            'shirt_and_pants_color': self.create_accessory_color_in_hex(shirt_and_pants_color),
            'shoes': self.create_item_from_type(5, shoes_type),
            'shoes_color': self.create_accessory_color_in_hex(shoes_color),
            'tail': self.create_item_from_type(6, tail_type),
            'tail_color': self.create_accessory_color_in_hex(tail_color)
        }

        # Delete rare items from dictionaries
        if add_crown:
            del self.basic_hat_options['1']
        if add_hippie:
            del self.basic_hat_options['27']
        if add_jester:
            del self.basic_hat_options['28']
        # Check for premium items
        if add_flamethrower:
            del self.basic_misc_options['5']

        return accessories_data
