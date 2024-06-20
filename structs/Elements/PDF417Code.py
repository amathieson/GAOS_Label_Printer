from dataclasses import asdict

import PIL.Image
from PIL import ImageDraw

from structs.LabelLayoutEngine import _Element, LabelData
import pdf417


class PDF417Code(_Element):
    _content: str = ""
    _box_mode: bool = False
    _fill_color: str = "black"
    _back_color: str = "white"

    def __init__(self, content, box_mode: bool = False, fill_color: str = "black", back_color: str = "white"):
        self._content = content
        self._box_mode = box_mode
        self._fill_color = fill_color
        self._back_color = back_color

    def get_code_text(self, data: LabelData) -> str:
        return self._content.format(**asdict(data))

    def render(self, image: PIL.Image, location: (int, int, int, int), data: LabelData, *args) -> None:
        draw = ImageDraw.Draw(image)
        if self._box_mode:
            draw.rectangle(location, outline="black", width=1)
            return

        scale = 20
        width = 9999
        img = None
        codes = pdf417.encode(self.get_code_text(data))
        while scale > 1 and width > (location[2] - location[0]):
            img = pdf417.render_image(codes, scale=scale, bg_color=self._back_color, fg_color=self._fill_color,
                                      padding=1)
            scale = scale - 1
            width = img.size[0]

        image.paste(img, (location[0], location[1]))
