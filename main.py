from interfaces._preview import previewPrinter
from interfaces.pTouchPrinter import pTouchPrinter
from structs.LabelLayoutEngine import LabelLayoutEngine, LabelData

_LabelLayoutEngine = None
_Printers = []

if __name__ == '__main__':
    _Printers.append(pTouchPrinter())
    _Printers.append(previewPrinter())
    _LabelLayoutEngine = LabelLayoutEngine()
    _LabelLayoutEngine.set_data(LabelData(AssetName="zzTest", AssetID="A1B2C3", AssetTags="Test",
                                          LocationName="zzLocation", LocationID="Z3Y2X1", ArrowDirection="NORTH"))

    for printer in _Printers:
        print(f"Printer: {printer.get_name()}\t-\t{len(printer.get_layouts())} Layout(s) loaded")
        for layout in printer.get_layouts():
            print(f"\t\t{layout.Name}")

    _Printers[0].print(_LabelLayoutEngine.renderLabel(_Printers[0].get_layouts()[0]),
                       dims=_Printers[0].get_layouts()[0].Dimensions)