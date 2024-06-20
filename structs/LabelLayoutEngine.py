from dataclasses import dataclass
from typing import Literal
import PIL.Image
import io

from PIL.Image import Image


@dataclass
class LabelData:
    AssetName: str
    AssetID: str
    AssetTags: str
    LocationID: str
    LocationName: str
    ArrowDirection: Literal["NORTH", "EAST", "SOUTH", "WEST"]


class _Element:
    def render(self, image: PIL.Image, location: (int, int, int, int), data: LabelData, *args) -> None:
        ...


@dataclass
class LabelLayout:
    Name: str
    Elements: [(_Element, (int, int, int, int))]
    Dimensions: (int, int)
    Background: str


class LabelLayoutEngine:
    _data: LabelData

    def set_data(self, data: LabelData):
        self._data = data

    def renderLabel(self, layout: LabelLayout) -> Image:
        image = PIL.Image.new('RGB', layout.Dimensions, layout.Background)
        for element_tuple in layout.Elements:
            element_tuple[0].render(image, element_tuple[1], self._data)
        return image
