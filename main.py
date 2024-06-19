from structs.Elements.Label import LabelElement
from structs.LabelLayoutEngine import LabelLayoutEngine, LabelLayout, LabelData

if __name__ == '__main__':
    _LabelLayoutEngine = LabelLayoutEngine()
    _LabelLayoutEngine.set_data(LabelData(AssetName="zzTest", AssetID="A1B2C3", AssetTags="Test", LocationName="zzLocation", LocationID="Z3Y2X1", ArrowDirection="NORTH"))
    _LabelLayoutEngine.renderLabel(LabelLayout(Name="TEST_LAYOUT", Elements=[
        (LabelElement("{AssetID}", font_name="NotoSansMono-Black"), (8, 8, 128, 64))
    ], Dimensions=(384, 216)))
