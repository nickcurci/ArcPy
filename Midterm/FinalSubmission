#This project will examine Blue Whales and Killer Whales sightings in
# Nova Scotia and assess their roaming area.
#Please download the fish csv file to your output directory
#Please download the Nova Scotia folder to out output directory as well

# Imports
import pandas
import os, arcpy
from arcpy.sa import *
#Set Environment
###########################################################
########### Set your Directory and Workspace ##############
###########################################################
outputDirectory = r"C:\data\d1\Midterm"
arcpy.env.workspace = outputDirectory
arcpy.env.overwriteOutput = True





# #Read the Fish CSV containing all sightings, group by species, split into datasets and send to CSV
import pandas as pd
data = pd.read_csv((os.path.join(outputDirectory,"Fish.csv")))
data_category_range = data['vernacularName'].unique()
data_category_range = data_category_range.tolist()
for i, value in enumerate(data_category_range):
    data[data['vernacularName'] == value].to_csv(r'vernacularName_'+str(value)+r'.csv', index=False, na_rep='N/A')





# Process One: Convert all datasets to shapefiles
import os, arcpy, pandas as pd
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
    # If an error occurred prin t the message to the screen
    print(arcpy.GetMessages())
print("files saved successfully")





#Process Two.1
#We will now buffer killer whales and blue whales at 50 miles
#Buffer Killer Whales for 50 Miles Range
KillerWhales = os.path.join(outputDirectory,"vernacularName_Whale_Killer.shp")
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





#Process Two.2
BlueWhales = os.path.join(outputDirectory,"vernacularName_Whale_Blue.shp")
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






#Process Three
#We will now intersect the Blue Whales and Killer Whales roaming areas at 50 miles.
BlueWhales_Buffer = os.path.join(outputDirectory,"BlueWhales_Buffer.shp")
KillerWhales_Buffer = os.path.join(outputDirectory,"KillerWhales_Buffer.shp")
Intersect_Whales = os.path.join(outputDirectory,"IntersectedWhales.shp")
arcpy.Intersect_analysis(in_features=[[BlueWhales_Buffer, ""], [KillerWhales_Buffer, ""]],
                         out_feature_class=Intersect_Whales, join_attributes="ALL",
                         cluster_tolerance="", output_type="INPUT")
print("intersect complete")






#Process Four
#we will now calculate the area of the intersected whales
##### DOES THIS NEED TO BE CHANGED BELOW?
arcpy.ImportToolbox(r"C:\Program Files\ArcGIS\Pro\Resources\ArcToolBox\Toolboxes\Data Management Tools.tbx")
IntersectedWhales = os.path.join(outputDirectory,"IntersectedWhales.shp")
# I actually dont think I need these two "AWhaleArea" lines but I'm not
# sure what the output would be without them
AWhaleArea = os.path.join(outputDirectory,"AWhaleArea.shp")
AWhaleArea = arcpy.AddGeometryAttributes_management(Input_Features=IntersectedWhales, Geometry_Properties=["AREA_GEODESIC"], Length_Unit="MILES_US", Area_Unit="SQUARE_MILES_US", Coordinate_System="GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")[0]
print("area calculation complete")






#Process Five
#Erase buffer areas that overlap Land
CanadaProvinces = os.path.join(outputDirectory,"NovaScotiaCounties\County_Polygons.shp")
FinalShapefile = os.path.join(outputDirectory,"FinalShapefiled.shp")
arcpy.Erase_analysis(in_features=IntersectedWhales, erase_features=CanadaProvinces,
                     out_feature_class=FinalShapefile, cluster_tolerance="")
print("Land Has Been Erased")
print("All processes have been completed successfully.")
print("The FinalShapefile.ship will show combined areas of Blue Whales and Killer Whales around Nova Scotia")
print("It can be found here: FinalShapefiled.shp whereever you decided to store it. ")
print("This is the end.")
