from enum import Enum
from .DataGenerator import DataGenerator
from .MonKey import MonKey
from .AccessoriesDataGenerator import AccessoriesDataGenerator


class MonKeyDataGenerator(DataGenerator):

    class Gender(Enum):
        Male = 1
        Female = 2

    class Status(Enum):
        Citizen = 1
        Junta = 2

    def __init__(self):
        super().__init__()
        self.junta_monKeys = ['ban_1h11mrypctfiexeo3swn1odo78uazf8oudrbqhcpzqyxjpu7eksrad8t1shg', # Randomizer
                              'ban_1yekta1xn94qdnbmmj1tqg76zk3apcfd31pjmuy6d879e3mr469a4o4sdhd4', # Yekta
                              'ban_3fudcakefr9jyw7b4kfafrgaekmd37ez7q4pmzuo1fd7wo9jo8gsha7z7e1c', # CFC
                              'ban_1wirginxksoeggr1u51a797tytmicokwnxxsosmd1q3mapuad4j6hdzeh617', # Not Idol
                              'ban_1bboss18y784j9rbwgt95uwqamjpsi9oips5syohsjk37rn5ud7ndbjq61ft', # bbedward
							  'ban_1ka1ium4pfue3uxtntqsrib8mumxgazsjf58gidh1xeo5te3whsq8z476goo', # Kalium Donations
							  'ban_1eska1qx1cd1x7tkbo4wmuofpsq69dekk7h5n6yo967kjq43nhhobrhno95x', # Eska
							  'ban_1cowcowypypjbhxbhmmcwmuurh8hnx45ycb36489zrxpq8e7fja5k1f19t59', # Cowello
							  'ban_1fomofudww7niykjtpzqgu9zpojtxx1f4pedjguk1gsrft44ere77sh1ky8g', # Snapdoodle
							  'ban_1creepi89mp48wkyg5fktgap9j6165d8yz6g1fbe5pneinz3by9o54fuq63m', # Creeper
							  'ban_1duckjfam7tcartyzk4eeouu17h7t8bpcjyyh4o31ih3qd7scz9w5a4u6qd4', # duck
							  'ban_31dhbgirwzd3ce7naor6o94woefws9hpxu4q8uxm1bz98w89zqpfks5rk3ad', # Mercatox
							  'ban_1monkeyt1x77a1rp9bwtthajb8odapbmnzpyt8357ac8a1bcron34i3r9y66'  # MonkeyTalks - Deadpool  
                              ]
        self.accessories_generator = AccessoriesDataGenerator()

    def create_gender(self, gender_character):
        # the addresses prefix is either ban_1 or ban_3. 1 will be male and 3 will be female
        return self.Gender.Male if gender_character ==  "1" else self.Gender.Female

    def create_status(self, banano_address):
        return self.Status.Junta if banano_address in self.junta_monKeys else self.Status.Citizen

    def generate_monKey_data_from_address(self, banano_address):

        # gender_character = banano_address[4]
        main_color_substring = banano_address[-13:-8]
        eye_color_substring = banano_address[-18:-13]
        fur_color = self.get_RGB_tuple_from_base32_number(main_color_substring)
        eye_color = self.get_RGB_tuple_from_base32_number(eye_color_substring)

        monKey_data = {

        "address": banano_address,
        # "gender": str(self.create_gender(gender_character).name),
        # "name": "monKey",
        "status": str(self.create_status(banano_address).name),
        "fur_color": fur_color + (255,),
        "fur_color_in_hex": '#%02x%02x%02x' % fur_color,
        "eye_color": eye_color + (255,),
        "eye_color_in_hex": '#%02x%02x%02x' % eye_color

        # Add attributes
        }
        return monKey_data

    def generate_monKey(self,banano_address):
        monKey_data = self.generate_monKey_data_from_address(banano_address)
        accessories_data = self.accessories_generator.generate_accessories_data_from_address(banano_address)
        monKey_data["accessories"] = accessories_data
        return MonKey(monKey_data)
