from dataclasses import dataclass
from typing import Literal
import PIL.Image


@dataclass
class LabelData:
    AssetName: str
    AssetID: str
    AssetTags: str
    LocationID: str
    LocationName: str
    ArrowDirection: Literal["NORTH", "EAST", "SOUTH", "WEST"]


class _Element:
    def render(self, location: (int, int, int, int), data: LabelData, *args) -> None:
        ...


@dataclass
class LabelLayout:
    Name: str
    Elements: [(_Element, (int, int, int, int))]
    Dimensions: (int, int)


class LabelLayoutEngine:
    def __init__(self):
        ...

    def renderLabel(self, layout: LabelLayout, data: LabelData):
        ...