import PIL.Image

from interfaces._printer import _PrinterInterface
from structs.Elements.ImageElement import ImageElement
from structs.Elements.Label import LabelElement
from structs.Elements.QRCode import QRCode
from structs.LabelLayoutEngine import LabelLayout
from pyPTouch.pTouchEnums import PrintSettings, AdvancedPrintSettings
from pyPTouch.pTouchPrinter import PTouchPrinter


class pTouchPrinter(_PrinterInterface):
    colours = {
        "White": (255, 255, 255),
        "Other": (192, 192, 192),
        "Clear": (240, 248, 255),
        "Red": (255, 0, 0),
        "Blue": (0, 0, 255),
        "Yellow": (255, 255, 0),
        "Green": (0, 128, 0),
        "Black": (0, 0, 0),
        "ClearWhiteText": (245, 245, 245),
        "MatteWhite": (245, 245, 220),
        "MatteClear": (248, 248, 255),
        "MatteSilver": (192, 192, 192),
        "SatinGold": (255, 215, 0),
        "SatinSilver": (192, 192, 192),
        "BlueD": (0, 0, 139),
        "RedD": (139, 0, 0),
        "FluorescentOrange": (255, 69, 0),
        "FluorescentYellow": (255, 255, 102),
        "BerryPinkS": (255, 20, 147),
        "LightGrayS": (211, 211, 211),
        "LimeGreenS": (50, 205, 50),
        "YellowF": (255, 255, 224),
        "PinkF": (255, 182, 193),
        "BlueF": (173, 216, 230),
        "WhiteHeatShrinkTube": (255, 255, 255),
        "WhiteFlexId": (255, 255, 255),
        "YellowFlexId": (255, 255, 0),
        "Cleaning": (255, 255, 255),
        "Stencil": (255, 255, 255),
        "Incompatible": (128, 128, 128),
    }

    def get_name(self) -> str:
        try:
            with PTouchPrinter() as printer:
                info = printer.get_information()
            return "Brother " + info.ModelCode.name
        except ValueError:
            return 'None'

    def get_layouts(self) -> [LabelLayout]:
        try:
            layouts = []
            with PTouchPrinter() as printer:
                info = printer.get_information()
                layouts.append(LabelLayout(f"PTouch STD {info.MediaWidth}mm {info.TextColour.name} on "
                                           f"{info.TapeColour.name} {info.MediaType.name}", [
                                               (
                                                   LabelElement("{AssetID}",
                                                                text_colour=self.colours[info.TextColour.name],
                                                                fill_colour=self.colours[info.TapeColour.name],
                                                                alignment="C",
                                                                font_name="NotoSansMono-Bold",
                                                                ),
                                                   (128, 40, 377, 116)),
                                               (QRCode(content="GAOS_{AssetID}"),
                                                (10, 10, 128, 128)),
                                               (ImageElement(path="GAOS-logo-black.png",
                                                             invert=(info.TextColour.name == "White")),
                                                (226, 14, 293, 49)),
                                           ], (391, 128), self.colours[info.TapeColour.name]))
            return layouts
        except ValueError:
            return []

    def get_additional_methods(self) -> [str]:
        return []

    def get_additional_parameters(self) -> [(str, str)]:
        return []

    def print(self, image: PIL.Image, dims: (int, int), **kwargs) -> None:
        with PTouchPrinter() as printer:
            info = printer.get_information()
            raster = []
            col1 = 1 if info.TextColour.name == "White" else 0
            col2 = 0 if col1 == 1 else 1
            for x in range(dims[0]):
                for i in range(16):
                    cur_byte = 0
                    for y in range(8):
                        r, g, b = image.getpixel((x, y + i * 8))
                        brightness = col1 if ((0.2126 * r) + (0.7152 * g) + (0.0722 * b)) > 128 else col2
                        cur_byte += brightness << (7 - y)
                    raster.append(cur_byte.to_bytes(length=1, byteorder='little'))

            printer.tape_width = info.MediaWidth  # Set the tape width based on the printer's media width
            printer.tape_length = 0  # Set tape length (0 typically means auto length)
            printer.media_type = info.MediaType  # Set media type based on printer's media type
            printer.print_settings = PrintSettings.AutoCut  # Enable automatic cutting after printing
            printer.advanced_settings = 0
            printer.print(b''.join(raster), dims[0], (14, 0))

    def call_method(self, method_name: str):
        return
