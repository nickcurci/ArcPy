import arcpy, os

#########################################
#### Change this to your Dir of the######
#### Zip file that you downloaded########
#########################################
outputDirectory = r"C:\data\d1\Final\Data"
arcpy.env.workspace = outputDirectory

print("Welcome to the whale toolbox. "
      "Here we will use multiple tools to show the similar ranging areas of multiple whale species")
class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Python Toolbox Whales"
        self.alias = "Python Toolbox Whales"

        # List of tool classes associated with this toolbox
        self.tools = [WhaleBuffer, WhaleIntersect, WhaleArea, WhaleErase]


class WhaleBuffer(object):
    print("We will begin with the Whale Buffer tool")
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Whale Buffer Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        print("Input Parameters")
        print("Inputting Parameters...")
        params = []
        input_shp1 = arcpy.Parameter(name="input_shp1",
                                     displayName="Input shp 1",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp1.value = os.path.join(outputDirectory, "input","WHALE_BLUE.shp")
        params.append(input_shp1)
        print("...Blue Whale Parameter added")
        print("...Adding second parameter")
        input_shp2 = arcpy.Parameter(name="input_shp2",
                                     displayName="Input shp 2",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp2.value = os.path.join(outputDirectory,"input","WHALE_Killer.shp")
        params.append(input_shp2)
        print("...Killer Whale Parameter added")
        print("Adding output parameter...")
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = os.path.join(outputDirectory,"output","WhaleBuffer.shp")
        params.append(output)
        print("...Output Parameter added")
        return params

    def isLicensed(self):
        print("checking license")
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
        print("Executing Buffer...")
        input_shp1 = parameters[0].valueAsText
        input_shp2 = parameters[1].valueAsText
        output = parameters[2].valueAsText
        arcpy.env.overwriteOutput = True
        Blue_Buffer = os.path.join(outputDirectory,"output","WHALE_Blue_Buffer.shp")
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

        Killer_Buffer = os.path.join(outputDirectory,"output","WHALE_Killer_Buffer.shp")
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
    print("We will now use the Intersect Tool")
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Whale Intersect Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        print("Adding Parameters...")
        print("...Adding Blue Whale Buffer")
        input_shp1 = arcpy.Parameter(name="input_shp1",
                                     displayName="Input shp 1",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp1.value = os.path.join(outputDirectory,"output","WHALE_BLUE_Buffer.shp")
        params.append(input_shp1)
        print("... Blue whale buffer added")
        print("Adding Killer Whale buffer...")
        input_shp2 = arcpy.Parameter(name="input_shp2",
                                     displayName="Input shp 2",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp2.value = os.path.join(outputDirectory,"output","WHALE_Killer_buffer.shp")
        params.append(input_shp2)
        print("...Killer Whale Buffer Added")
        print("Adding output parameter...")
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = os.path.join(outputDirectory,"output","Intersect.shp")
        params.append(output)
        print("...Output parameter added")
        print("All parameters added")
        return params

    def isLicensed(self):
        print("checking license...")
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
        print("Executing the Intersect")
        input_shp1 = parameters[0].valueAsText
        input_shp2 = parameters[1].valueAsText
        output = parameters[2].valueAsText
        arcpy.env.overwriteOutput = True
        intersect_whales = os.path.join(outputDirectory,"output","Intersect.shp")
        print("Starting Intersect...")
        arcpy.Intersect_analysis(in_features=(input_shp1, input_shp2),
                                 out_feature_class=intersect_whales, join_attributes="ALL",
                                 cluster_tolerance="", output_type="INPUT")
        print(".. Intersect complete")
        return

class WhaleArea(object):
    print("We will now use the Area tool")
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Whale Area Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        print("Adding Parameters")
        print("Adding Intersect parameter...")
        params = []
        input_shp1 = arcpy.Parameter(name="input_shp1",
                                     displayName="Input shp 1",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp1.value = os.path.join(outputDirectory,"output","Intersect.shp")
        params.append(input_shp1)
        print("...Intersect Parameter Added")
        print("Adding output parameter...")
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Optional",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = os.path.join(outputDirectory,"output","Intersect.shp")
        params.append(output)
        print("...output parameter added")
        print("All Parameters added")
        return params

    def isLicensed(self):
        print("Checking License")
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
        print("Executing Area Tool")
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
    print("We will now use the Erase Tool")
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Whale Erase Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        print("Adding parameters")
        print("Adding intersect parameter...")
        params = []
        input_shp1 = arcpy.Parameter(name="input_shp1",
                                     displayName="Input shp 1",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp1.value = os.path.join(outputDirectory,"output","intersect.shp")
        params.append(input_shp1)
        print("...Intersect parameter added")
        print("Adding Nova Scotia Polygons Parameter...")
        input_shp2 = arcpy.Parameter(name="input_shp2",
                                     displayName="Input shp 2",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input_shp2.value = os.path.join(outputDirectory,"NovaScotiaCounties","County_Polygons.shp")
        params.append(input_shp2)
        print("...Nova Scotia Added")
        print("Adding output parameter...")
        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = os.path.join(outputDirectory,"FinalShapefile.shp")
        params.append(output)
        print("...output parameter added")
        print("All Parameters added")
        return params

    def isLicensed(self):
        print("Cecking License")
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
        print("Executing Erase Tool")
        input_shp1 = parameters[0].valueAsText
        input_shp2 = parameters[1].valueAsText
        output = parameters[2].valueAsText
        arcpy.env.overwriteOutput = True
        FinalShapefile = os.path.join(outputDirectory,"Final_Shapefile.shp")
        print("Starting Erase...")
        arcpy.Erase_analysis(in_features=input_shp1, erase_features=input_shp2,
                             out_feature_class=FinalShapefile, cluster_tolerance="")
        print("...Erase analysis done.")
        print("All processes done")
        return

# Run the Tools without having to go into ArcPro
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