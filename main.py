from structs.LabelLayoutEngine import LabelLayoutEngine, LabelLayout, LabelData

if __name__ == '__main__':
    _LabelLayoutEngine = LabelLayoutEngine()
    _LabelLayoutEngine.renderLabel(LabelLayout(Name="TEST_LAYOUT", Elements=[], Dimensions=(512, 128)), LabelData(AssetName="zzTest", AssetID="A1B2C3", AssetTags="Test", LocationName="zzLocation", LocationID="Z3Y2X1", ArrowDirection="NORTH"))
