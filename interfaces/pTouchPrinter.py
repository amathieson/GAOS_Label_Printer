import PIL.Image
from pyPTouch.pTouchStatusInformation import StatusInformation

from interfaces._printer import _PrinterInterface
from structs.Elements.ImageElement import ImageElement
from structs.Elements.Label import LabelElement
from structs.Elements.QRCode import QRCode
from structs.LabelLayoutEngine import LabelLayout
from pyPTouch.pTouchEnums import *
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
        layouts = []
        try:
            with PTouchPrinter() as printer:
                info = printer.get_information()
        except ValueError:
            info = StatusInformation(
                HeadMark=0x80,
                Size=0x20,
                BrotherCode=0x42,
                SeriesCode=0x30,
                ModelCode=ModelCode(0x64),
                CountryCode=0x30,
                BatteryLevel=BatteryLevel.Unknown,
                ExtendedError=ExtendedError.NoError,
                ErrorInfo1=ErrorInfo1.NoError,
                ErrorInfo2=ErrorInfo2.NoError,
                MediaWidth=18,
                MediaType=MediaType.LaminatedTape,
                NumberColours=0,
                Fonts=0,
                JapaneseFonts=0,
                Mode=DynamicMode.Raster,
                Density=0,
                MediaLength=0,
                StatusType=StatusType.Reply_To_Status,
                PhaseType=PhaseType.Editing,
                PhaseNumber=0,
                NotificationType=NotificationType.NotAvailable,
                ExpansionArea=0,
                TapeColour=TapeColor.Black,
                TextColour=TextColor.White,
                HardwareSettings=0,
                Reserved3=0,
                Reserved4=0,
            )
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

        layouts.append(LabelLayout(f"PTouch Cable STD {info.MediaWidth}mm {info.TextColour.name} on "
                                   f"{info.TapeColour.name} {info.MediaType.name}", [
                                       (
                                           LabelElement("{AssetID}",
                                                        text_colour=self.colours[info.TextColour.name],
                                                        fill_colour=self.colours[info.TapeColour.name],
                                                        alignment="C",
                                                        font_name="NotoSansMono-Bold",
                                                        ),
                                           (45, 0, 145, 15)),
                                       (LabelElement("{AssetID}",
                                                     text_colour=self.colours[info.TextColour.name],
                                                     fill_colour=self.colours[info.TapeColour.name],
                                                     alignment="C",
                                                     font_name="NotoSansMono-Bold",
                                                     ),
                                        (45, 20, 145, 35)),
                                       (LabelElement("{AssetID}",
                                                     text_colour=self.colours[info.TextColour.name],
                                                     fill_colour=self.colours[info.TapeColour.name],
                                                     alignment="C",
                                                     font_name="NotoSansMono-Bold",
                                                     ),
                                        (45, 40, 145, 55)),
                                       (LabelElement("{AssetID}",
                                                     text_colour=self.colours[info.TextColour.name],
                                                     fill_colour=self.colours[info.TapeColour.name],
                                                     alignment="C",
                                                     font_name="NotoSansMono-Bold",
                                                     ),
                                        (45, 60, 145, 75)),
                                       (LabelElement("{AssetID}",
                                                     text_colour=self.colours[info.TextColour.name],
                                                     fill_colour=self.colours[info.TapeColour.name],
                                                     alignment="C",
                                                     font_name="NotoSansMono-Bold",
                                                     ),
                                        (45, 80, 145, 95)),
                                       (LabelElement("{AssetID}",
                                                     text_colour=self.colours[info.TextColour.name],
                                                     fill_colour=self.colours[info.TapeColour.name],
                                                     alignment="C",
                                                     font_name="NotoSansMono-Bold",
                                                     ),
                                        (45, 100, 145, 115)),
                                       # (BarCode(content="{AssetID}", format="code39"),
                                       #  (0, 0, 200, 128)),
                                       (ImageElement(path="GAOS-logo-black90.png",
                                                     invert=(info.TextColour.name == "White")),
                                        (5, 5, 40, 72)),
                                   ], (140, 128), self.colours[info.TapeColour.name]))

        layouts.append(LabelLayout(f"PTouch Mini-XLR Mic Cables {info.MediaWidth}mm {info.TextColour.name} on "
                                   f"{info.TapeColour.name} {info.MediaType.name}", [
                                       (
                                           LabelElement("{AssetID}",
                                                        text_colour=self.colours[info.TextColour.name],
                                                        fill_colour=self.colours[info.TapeColour.name],
                                                        alignment="C",
                                                        font_name="NotoSansMono-Bold",
                                                        ),
                                           (128, 40, 377, 75)),
                                       (
                                           LabelElement("|",
                                                        text_colour=self.colours[info.TextColour.name],
                                                        fill_colour=self.colours[info.TapeColour.name],
                                                        alignment="L",
                                                        font_name="NotoSans-Light",
                                                        ),
                                           (391, 0, 398, 128)),
                                       (
                                           LabelElement("|",
                                                        text_colour=self.colours[info.TextColour.name],
                                                        fill_colour=self.colours[info.TapeColour.name],
                                                        alignment="L",
                                                        font_name="NotoSans-Light",
                                                        ),
                                           (391, 16, 398, 128)),
                                       (
                                           LabelElement("|",
                                                        text_colour=self.colours[info.TextColour.name],
                                                        fill_colour=self.colours[info.TapeColour.name],
                                                        alignment="L",
                                                        font_name="NotoSans-Light",
                                                        ),
                                           (391, 32, 398, 128)),
                                       (
                                           LabelElement("|",
                                                        text_colour=self.colours[info.TextColour.name],
                                                        fill_colour=self.colours[info.TapeColour.name],
                                                        alignment="L",
                                                        font_name="NotoSans-Light",
                                                        ),
                                           (391, 48, 398, 128)),
                                       (
                                           LabelElement("|",
                                                        text_colour=self.colours[info.TextColour.name],
                                                        fill_colour=self.colours[info.TapeColour.name],
                                                        alignment="L",
                                                        font_name="NotoSans-Light",
                                                        ),
                                           (391, 64, 398, 128)),
                                       (
                                           LabelElement("|",
                                                        text_colour=self.colours[info.TextColour.name],
                                                        fill_colour=self.colours[info.TapeColour.name],
                                                        alignment="L",
                                                        font_name="NotoSans-Light",
                                                        ),
                                           (391, 80, 398, 128)),
                                       (
                                           LabelElement("|",
                                                        text_colour=self.colours[info.TextColour.name],
                                                        fill_colour=self.colours[info.TapeColour.name],
                                                        alignment="L",
                                                        font_name="NotoSans-Light",
                                                        ),
                                           (391, 96, 398, 128)),
                                       (
                                           LabelElement("|",
                                                        text_colour=self.colours[info.TextColour.name],
                                                        fill_colour=self.colours[info.TapeColour.name],
                                                        alignment="L",
                                                        font_name="NotoSans-Light",
                                                        ),
                                           (391, 112, 398, 128)),
                                       (
                                           LabelElement("{AssetID:<2}",
                                                        text_colour=self.colours[info.TextColour.name],
                                                        fill_colour=self.colours[info.TapeColour.name],
                                                        alignment="C",
                                                        font_name="NotoSansMono_ExtraCondensed-Light",
                                                        ),
                                           (410, 0, 450, 64)),
                                       (
                                           LabelElement("{AssetID:<2}",
                                                        text_colour=self.colours[info.TextColour.name],
                                                        fill_colour=self.colours[info.TapeColour.name],
                                                        alignment="C",
                                                        font_name="NotoSansMono_ExtraCondensed-Light",
                                                        ),
                                           (410, 64, 450, 128)),
                                       (
                                           LabelElement("{AssetName}",
                                                        text_colour=self.colours[info.TextColour.name],
                                                        fill_colour=self.colours[info.TapeColour.name],
                                                        alignment="C",
                                                        font_name="NotoSans-Light",
                                                        ),
                                           (128, 90, 377, 110)),
                                       (QRCode(content="GAOS_{AssetID:_<6}"),
                                        (10, 10, 128, 128)),
                                       (ImageElement(path="GAOS-logo-black.png",
                                                     invert=(info.TextColour.name == "White")),
                                        (215, 14, 293, 49)),
                                   ], (465, 128), self.colours[info.TapeColour.name]))
        layouts.append(LabelLayout(f"PTouch 2x Mic Cable Flags {info.MediaWidth}mm {info.TextColour.name} on "
                                   f"{info.TapeColour.name} {info.MediaType.name}", [
                                       (
                                           LabelElement("{AssetID}",
                                                        text_colour=self.colours[info.TextColour.name],
                                                        fill_colour=self.colours[info.TapeColour.name],
                                                        alignment="C",
                                                        font_name="NotoSansMono-Bold",
                                                        ),
                                           (7, 2, 64, 64)),
                                       (
                                           QRCode(content="GAOS_{AssetID:_<6}",
                                                  fill_color=self.colours[info.TextColour.name],
                                                  back_color=self.colours[info.TapeColour.name] ),
                                           (94, 9, 64, 64)
                                       ),
                                       (ImageElement(path="GAOS-logo-black.png",
                                                     invert=(info.TextColour.name == "White")),
                                        (0, 79, 64, 112)),
                                       (ImageElement(path="GAOS-logo-black.png",
                                                     invert=(info.TextColour.name == "White")),
                                        (92, 79, 156, 112))
                                   ], (156, 128), self.colours[info.TapeColour.name]))
        return layouts

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
