from structs.Elements.Label import LabelElement
from structs.Elements.PDF417Code import PDF417Code
from structs.Elements.QRCode import QRCode
from structs.Elements.ImageElement import ImageElement
from structs.LabelLayoutEngine import LabelLayoutEngine, LabelLayout, LabelData

if __name__ == '__main__':
    _LabelLayoutEngine = LabelLayoutEngine()
    _LabelLayoutEngine.set_data(LabelData(AssetName="zzTest", AssetID="A1B2C3", AssetTags="Test", LocationName="zzLocation", LocationID="Z3Y2X1", ArrowDirection="NORTH"))
    _LabelLayoutEngine.renderLabel(LabelLayout(Name="TEST_LAYOUT", Elements=[
        (LabelElement("Asset: {AssetID}", font_name="NotoSansMono-Black", alignment="C"), (8, 8, 128, 64)),
        (QRCode("GAOS_{AssetID}"), (128, 0, 256, 128)),
        (ImageElement("GAOS-logo-black.png"), (32, 32, 93, 64)),
        (PDF417Code("GAOS_{AssetID}"), (0, 170, 300, 300)),
    ], Dimensions=(384, 216)))
