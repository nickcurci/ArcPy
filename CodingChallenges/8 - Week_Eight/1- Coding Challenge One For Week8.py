
# This function takes in two CSV Files, transforms them to shapefiles, and then buffers them both before intersecting them.
# We will use the Killer Whale and Blue Whale sighting CSV files to determine their roaming area
import os, arcpy
from arcpy.sa import *
###################################
######### SET YOUR DIR#############
###################################
outputDirectory = r"C:\data\d1\8\data"
arcpy.env.workspace = outputDirectory
arcpy.env.overwriteOutput = True
#Convert cvs files to shapefiles
def buffer(x, y):
    csvlist = arcpy.ListFiles("*.csv")
    try:
        for csvfile in csvlist:
            outlayer = "CSVEventLayer"
            spatialreference = "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision"
            arcpy.MakeXYEventLayer_management(csvfile, "decimalLongitude", "decimalLatitude", outlayer, spatialreference, "#")

            shpfile = os.path.splitext(csvfile.replace('-', '_'))[0]
            arcpy.CopyFeatures_management(outlayer,shpfile)
        del outlayer
    except:
    # If an error occurred print the message to the screen
        print(arcpy.GetMessages())
    print("shapefiles created successfully")

#Process One.1

    KillerWhales = os.path.join(outputDirectory, x)
    Buffered_KillerWhales = os.path.join(outputDirectory,"KillerWhales_Buffer.shp")
    arcpy.analysis.Buffer(in_features=KillerWhales,
                          out_feature_class=Buffered_KillerWhales,
                          buffer_distance_or_field="50 Miles",
                          line_side="FULL",
                          line_end_type="ROUND",
                          dissolve_option="ALL",
                          dissolve_field=[],
                          method="PLANAR")
    arcpy.env.overwriteOutput = True
    print("buffer one complete")



    #Process One.2
    BlueWhales = os.path.join(outputDirectory, y)
    Buffered_BlueWhales = os.path.join(outputDirectory,"BlueWhales_Buffer.shp")
    arcpy.analysis.Buffer(in_features=BlueWhales,
                          out_feature_class=Buffered_BlueWhales,
                          buffer_distance_or_field="50 Miles",
                          line_side="FULL",
                          line_end_type="ROUND",
                          dissolve_option="ALL",
                          dissolve_field=[],
                          method="PLANAR")

    print("buffer two complete")



#Process Two
#We will now intersect the Blue Whales and Killer Whales roaming areas at 50 miles.
    BlueWhales_Buffer = os.path.join(outputDirectory,"BlueWhales_Buffer.shp")
    KillerWhales_Buffer = os.path.join(outputDirectory,"KillerWhales_Buffer.shp")
    Intersect_Whales = os.path.join(outputDirectory,"IntersectedWhales.shp")
    arcpy.Intersect_analysis(in_features=[[BlueWhales_Buffer, ""], [KillerWhales_Buffer, ""]],
                         out_feature_class=Intersect_Whales, join_attributes="ALL",
                         cluster_tolerance="", output_type="INPUT")
    print("intersect complete")
    return

buffer("vernacularName_Whale_Killer.shp","vernacularName_Whale_Blue.shp")
print("The function is complete, please view your file at 'IntersectedWhales.shp'")
