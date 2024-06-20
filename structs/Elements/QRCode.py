from dataclasses import asdict

import PIL.Image
from PIL import ImageDraw

from structs.LabelLayoutEngine import _Element, LabelData
import qrcode


class QRCode(_Element):
    _content: str = ""
    _box_mode: bool = False
    _fill_color: str = "black"
    _back_color: str = "white"

    def __init__(self, content, box_mode: bool = False, fill_color: str = "black", back_color: str = "white"):
        self._content = content
        self._box_mode = box_mode
        self._fill_color = fill_color
        self._back_color = back_color

    def get_qr_text(self, data: LabelData) -> str:
        return self._content.format(**asdict(data))

    def render(self, image: PIL.Image, location: (int, int, int, int), data: LabelData, *args) -> None:
        draw = ImageDraw.Draw(image)
        if self._box_mode:
            draw.rectangle(location, outline="black", width=1)
            return

        box_size = 20
        width = 9999
        img = None
        while box_size > 1 and width > (location[2] - location[0]):
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=box_size,
                border=1,
            )
            box_size -= 1
            qr.add_data(self.get_qr_text(data))
            qr.make(fit=True)
            img = qr.make_image(fill_color=self._fill_color, back_color=self._back_color)
            width = img.size[0]

        image.paste(img, (location[0], location[1]))
