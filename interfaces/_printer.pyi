from structs.LabelLayoutEngine import LabelLayout


class _PrinterInterface:
    def get_name(self) -> str:
        ...

    def get_layouts(self) -> [LabelLayout]:
        ...

    def get_additional_methods(self) -> [str]:
        ...

    def get_additional_parameters(self) -> [(str, str)]:
        ...

    def print(self, args: object) -> None:
        ...

    def call_method(self, method_name: str):
        ...
