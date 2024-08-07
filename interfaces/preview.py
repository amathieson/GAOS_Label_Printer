import PIL.Image

from interfaces._printer import _PrinterInterface
from structs.LabelLayoutEngine import LabelLayout


class previewPrinter(_PrinterInterface):
    def get_name(self) -> str:
        return 'Preview'

    def get_layouts(self) -> [LabelLayout]:
            return []

    def get_additional_methods(self) -> [str]:
        return []

    def get_additional_parameters(self) -> [(str, str)]:
        return []

    def print(self, image: PIL.Image, dims: (int, int), **kwargs) -> None:
        image.show()

    def call_method(self, method_name: str):
        return
