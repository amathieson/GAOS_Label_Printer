from dataclasses import dataclass
from typing import Literal


@dataclass
class LabelData:
    AssetName: str
    AssetID: str
    AssetTags: str
    LocationID: str
    LocationName: str
    ArrowDirection: Literal["NORTH", "EAST", "SOUTH", "WEST"] or None
