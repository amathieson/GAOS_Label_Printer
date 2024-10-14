from data.DataFactory import DataFactory
from interfaces.preview import previewPrinter
from interfaces.pTouchPrinter import pTouchPrinter
from structs.LabelLayoutEngine import LabelLayoutEngine

_LabelLayoutEngine = None
_Printers = []
_DataFactory = None

if __name__ == '__main__':
    _DataFactory = DataFactory()
    _Printers.append(pTouchPrinter())
    _Printers.append(previewPrinter())
    _LabelLayoutEngine = LabelLayoutEngine()
    asset = _DataFactory.fetch_asset("AB")
    _LabelLayoutEngine.set_data(asset)

    for printer in _Printers:
        print(f"Printer: {printer.get_name()}\t-\t{len(printer.get_layouts())} Layout(s) loaded")
        for layout in printer.get_layouts():
            print(f"\t\t{layout.Name}")

    _Printers[1].print(_LabelLayoutEngine.renderLabel(_Printers[0].get_layouts()[3]),
                       dims=_Printers[0].get_layouts()[3].Dimensions)
