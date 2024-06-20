import math
from typing import Literal

import PIL.Image
from PIL import ImageDraw, ImageFont

from structs.LabelLayoutEngine import _Element, LabelData
from dataclasses import asdict


class LabelElement(_Element):
    _label_text: str = ""
    _text_colour: str = "black"
    _fill_colour: str = "white"
    _font_name: str = "NotoSans-Medium"
    _box_mode: bool = False
    _alignment: Literal["L", "C", "R"] = "L"

    def __init__(self, label_text: str, text_colour: str = "black", fill_colour: str = "white",
                 font_name: str = "NotoSans-Medium", box_mode: bool = False, alignment: Literal["L", "C", "R"] = "L"):
        self._label_text = label_text
        self._text_colour = text_colour
        self._fill_colour = fill_colour
        self._font_name = font_name
        self._box_mode = box_mode
        self._alignment = alignment

    def get_label_text(self, data: LabelData) -> str:
        return self._label_text.format(**asdict(data))

    def render(self, image: PIL.Image, location: (int, int, int, int), data: LabelData, **kwargs) -> None:
        draw = ImageDraw.Draw(image)
        if self._box_mode:
            draw.rectangle(location, outline=self._text_colour, width=1)
            return

        draw.rectangle(location, fill=self._fill_colour)
        dims, fnt = self.calculate_size(data, location)
        if self._alignment == "L": # Kinda pointless but whatever...
            location = [location[0], *location[1:3]]
        if self._alignment == "C":
            x = ((location[2] - location[0]) - (dims[2] - dims[0])) / 2
            location = [location[0] + x, *location[1:3]]
        if self._alignment == "R":
            x = (dims[2] - dims[0])
            location = [location[2] - x, *location[1:3]]
        draw.text(location, self.get_label_text(data), fill=self._text_colour, font=fnt)

    def calculate_size(self, data: LabelData, location: (int, int, int, int)):
        font_size = 100
        size = None
        font = None
        while ((size is None or (size[2] - size[0]) > location[2] - location[0] or (size[3] - size[1]) > location[3]
                - location[1]) and
               font_size > 0):
            font = ImageFont.truetype("res/fonts/" + self._font_name + ".ttf", font_size)
            size = font.getbbox(self.get_label_text(data))
            font_size -= 1
        return size, font
