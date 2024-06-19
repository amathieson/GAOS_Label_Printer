import math

import PIL.Image
from PIL import ImageDraw, ImageFont

from structs.LabelLayoutEngine import _Element, LabelData


class LabelElement(_Element):
    _label_text: str = ""
    _text_colour: str = "black"
    _fill_colour: str = "white"
    _font_name: str = "NotoSansMono-VariableFont_wdth,wght"

    def __init__(self, label_text: str, text_colour: str = "black", fill_colour: str = "red",
                 font_name: str = "NotoSansMono-VariableFont_wdth,wght"):
        self._label_text = label_text
        self._text_colour = text_colour
        self._fill_colour = fill_colour
        self._font_name = font_name

    def render(self, image: PIL.Image, location: (int, int, int, int), data: LabelData, *args) -> None:
        draw = ImageDraw.Draw(image)
        draw.rectangle(location, fill=self._fill_colour)
        dims, fnt = self.calculate_size(data, location)
        if True: #.alignment:
            if True:# or args.alignment == "C":
                x = ((location[2] - location[0]) - (dims[2] - dims[0])) / 2
                location = [location[0] + x, *location[1:3]]
        draw.text(location, self._label_text, fill=self._text_colour, font=fnt)

    def calculate_size(self, data: LabelData, location: (int, int, int, int)):
        font_size = 100
        size = None
        font = None
        while ((size is None or (size[2] - size[0]) > location[2] - location[0] or (size[3] - size[1]) > location[3] - location[1]) and
               font_size > 0):
            font = ImageFont.truetype("res/fonts/" + self._font_name + ".ttf", font_size)
            size = font.getbbox(self._label_text)
            font_size -= 1
        return size, font
