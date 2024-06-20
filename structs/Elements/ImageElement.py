import PIL
from PIL import ImageDraw, Image
from PIL.Image import Resampling

from structs.LabelLayoutEngine import _Element, LabelData


class ImageElement(_Element):
    _path: str = ""
    _box_mode: bool = False

    def __init__(self, path: str, box_mode: bool = False) -> None:
        self._path = path
        self._box_mode = box_mode

    def render(self, image: PIL.Image, location: (int, int, int, int), data: LabelData, *args) -> None:
        draw = ImageDraw.Draw(image)
        if self._box_mode:
            draw.rectangle(location, outline="black", width=1)
            return

        vector = Image.open("res/images/" + self._path)
        dims = (location[2]-location[0], location[3]-location[1])
        i = vector.resize(dims, resample=Resampling.BILINEAR)
        image.paste(i, (location[0], location[1]), i)
