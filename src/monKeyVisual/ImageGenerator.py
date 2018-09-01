from svgimgutils import SVGAppender as SVGA
from cairosvg import svg2png
from io import BytesIO
import colorsys


class ImageGenerator:

    def generate_monKey_image(self, monKey, change_background_color='nobg', format='svg', accessories_level='full'):

        monkey_image = SVGA.fromfile('src/monKeyVisual/svg/monkey.svg')
        background_color = None
        # If a background is needed
        if change_background_color is not 'nobg':
            background_color = self.generate_background_color(monKey.fur_color)
        monkey_image.monkeycolorchange(monKey.fur_color_in_hex, monKey.eye_color_in_hex, background_color)
        # If monKey accessories_level is 'full' there will be a need for accessories addition
        if accessories_level is 'full':
            self.add_accessories(monKey,monkey_image)
        # If format is png
        if format == 'png':
            output = BytesIO()
            svg2png(bytestring=monkey_image.to_str(), write_to=output)
            contents = output.getvalue()
            output.close()
            return contents
        return monkey_image.to_str()

    def generate_background_color(self, fur_color):
        fur_color_hsv = colorsys.rgb_to_hsv(fur_color[0]/255, fur_color[1]/255, fur_color[2]/255)
        # H = Hue stays the same
        # S = Divide saturation by 4
        new_s = fur_color_hsv[1] / 4
        # V = Make value(brightness) always 1
        rgb_background_color = colorsys.hsv_to_rgb(fur_color_hsv[0], new_s, 1)
        return '#%02x%02x%02x' % (int(rgb_background_color[0] * 255), int(rgb_background_color[1] * 255), int(rgb_background_color[2] * 255))

    def add_accessories(self,monKey, monkey_image):
        for accessories_list in monKey.accessories:
            accessory = accessories_list[0]
            if accessory is not None:
                accessory_path = 'src/monKeyVisual/svg/accessories/' + accessory.item + '/' + accessory.value.lower() + '/' + accessory.type + '.svg'
                accessory_image = SVGA.fromfile(accessory_path)
                accessory_color = None
                # If the accessory is colorable
                if hasattr(accessory, 'color'):
                    accessory_color = accessory.color
                monkey_image.append(accessory_image, accessory_color)
