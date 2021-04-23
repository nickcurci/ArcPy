import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Python Toolbox Whales"
        self.alias = "Python Toolbox Whales"

        # List of tool classes associated with this toolbox
        self.tools = [WhaleBuffer, WhaleIntersect, WhaleArea, WhaleErase]


class WhaleBuffer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Whale Buffer Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_shp1 = arcpy.Parameter(name="input_shp1",
                                     displayName="Input shp 1",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp1.value = r"C:\data\d1\Final\data\input\WHALE_BLUE.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_shp1)

        input_shp2 = arcpy.Parameter(name="input_shp2",
                                     displayName="Input shp 2",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp2.value = r"C:\data\d1\Final\data\input\WHALE_Killer.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_shp2)

        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = r"C:\data\d1\Final\output\WhaleBuffer.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_shp1 = parameters[0].valueAsText
        input_shp2 = parameters[1].valueAsText
        output = parameters[2].valueAsText
        arcpy.env.overwriteOutput = True
        Blue_Buffer = 'C:\data\d1\Final\data\output\WHALE_Blue_Buffer.shp'
        arcpy.analysis.Buffer(in_features=input_shp1,
                              out_feature_class= Blue_Buffer,
                              buffer_distance_or_field="50 Miles",
                              line_side="FULL",
                              line_end_type="ROUND",
                              dissolve_option="ALL",
                              dissolve_field=[],
                              method="PLANAR")
        print("Starting Tool...")
        print("...Buffer 1 complete")

        Killer_Buffer = 'C:\data\d1\Final\data\output\WHALE_Killer_Buffer.shp'
        arcpy.analysis.Buffer(in_features=input_shp2,
                              out_feature_class= Killer_Buffer,
                              buffer_distance_or_field="50 Miles",
                              line_side="FULL",
                              line_end_type="ROUND",
                              dissolve_option="ALL",
                              dissolve_field=[],
                              method="PLANAR")
        print("...Buffer 2 complete")
        print("All Buffers Complete")
        return

class WhaleIntersect(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Whale Intersect Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_shp1 = arcpy.Parameter(name="input_shp1",
                                     displayName="Input shp 1",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp1.value = r"C:\data\d1\Final\data\output\WHALE_BLUE_Buffer.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_shp1)

        input_shp2 = arcpy.Parameter(name="input_shp2",
                                     displayName="Input shp 2",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp2.value = r"C:\data\d1\Final\data\output\WHALE_Killer_buffer.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_shp2)

        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = r"C:\data\d1\Final\output\Intersect.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_shp1 = parameters[0].valueAsText
        input_shp2 = parameters[1].valueAsText
        output = parameters[2].valueAsText
        arcpy.env.overwriteOutput = True
        intersect_whales = r'C:\data\d1\Final\data\output\Intersect.shp'
        print("Starting Intersect...")
        arcpy.Intersect_analysis(in_features=(input_shp1, input_shp2),
                                 out_feature_class=intersect_whales, join_attributes="ALL",
                                 cluster_tolerance="", output_type="INPUT")
        print(".. Intersect complete")
        return

class WhaleArea(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Whale Area Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_shp1 = arcpy.Parameter(name="input_shp1",
                                     displayName="Input shp 1",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp1.value = r"C:\data\d1\Final\data\output\Intersect.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_shp1)

        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Optional",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = r"C:\data\d1\Final\output\Intersect.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_shp1 = parameters[0].valueAsText
        output = parameters[1].valueAsText
        arcpy.env.overwriteOutput = True
        print("Starting Area Calculation")
        arcpy.AddGeometryAttributes_management(Input_Features=input_shp1,
                                               Geometry_Properties=["AREA_GEODESIC"],
                                               Length_Unit="MILES_US", Area_Unit="SQUARE_MILES_US",
                                               Coordinate_System="GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',"
                                                                 "SPHEROID['WGS_1984',6378137.0,298.257223563]],"
                                                                 "PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")
        print("... Running area calculation")
        print("Area calculation complete")

class WhaleErase(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Whale Erase Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_shp1 = arcpy.Parameter(name="input_shp1",
                                     displayName="Input shp 1",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp1.value = r"C:\data\d1\Final\data\output\intersect.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_shp1)

        input_shp2 = arcpy.Parameter(name="input_shp2",
                                     displayName="Input shp 2",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp2.value = r"C:\data\d1\Final\data\NovaScotiaCounties\County_Polygons.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_shp2)

        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = r"C:\data\d1\Final\FinalShapefile.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_shp1 = parameters[0].valueAsText
        input_shp2 = parameters[1].valueAsText
        output = parameters[2].valueAsText
        arcpy.env.overwriteOutput = True
        FinalShapefile = r'C:\data\d1\Final\data\Final_Shapefile.shp'
        print("Starting Erase...")
        arcpy.Erase_analysis(in_features=input_shp1, erase_features=input_shp2,
                             out_feature_class=FinalShapefile, cluster_tolerance="")
        print("...Erase analysis done.")
        print("All processes done")
        return

# This code block allows you to run your code in a test-mode within PyCharm, i.e. you do not have to open the tool in
# ArcMap. This works best for a "single tool" within the Toolbox.
def main():

    tool1 = WhaleBuffer()
    tool1.execute(tool1.getParameterInfo(), None)
    tool2 = WhaleIntersect()
    tool2.execute(tool2.getParameterInfo(), None)
    tool3 = WhaleArea()
    tool3.execute(tool3.getParameterInfo(), None)
    tool4 = WhaleErase()
    tool4.execute(tool4.getParameterInfo(), None)

if __name__ == '__main__':
    main()