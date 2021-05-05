##### Imports
import arcpy
import pandas
#Set Enviornment
arcpy.env.overwriteOutput = True  # If you get "already exists error" even when True, ensure file is not open.

#Read the CSV, group by species, split into two datasets and send to CSV
df = pandas.read_csv(r"C:\Data\d1\5\All_Files\AllWhales.csv")
groupedWhales = df.groupby(df.vernacularName)
print(groupedWhales)
Sperm = groupedWhales.get_group("WHALE-SPERM")
Right = groupedWhales.get_group("WHALE-RIGHT")
Sperm.to_csv(r"C:\Data\d1\5\All_Files\SpermWhales.csv")
Right.to_csv(r"C:\Data\d1\5\All_Files\RightWhales.csv")

#Convert first dataset into shapefile
arcpy.env.workspace = r"C:\Data\d1\5\ALL_FILES"
in_Table = r"SpermWhales.csv"
x_coords = "decimalLatitude"
y_coords = "decimalLongitude"
out_Layer = "SpermWhales"
saved_Layer = r"SpermWhales_Output.shp"
#set spatial reference
spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984
lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, "")
#check the number of records
print(arcpy.GetCount_management(out_Layer))
#save to a layer file
arcpy.CopyFeatures_management(lyr, saved_Layer)
if arcpy.Exists(saved_Layer):
    print("Created file successfully!")
#extact the Extent(XMin, XMax, YMin, YMax) of the shapefile.
desc = arcpy.Describe(saved_Layer)
XMin = desc.extent.XMin
XMax = desc.extent.XMax
YMin = desc.extent.YMin
YMax = desc.extent.YMax

#Generate a fishnet
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
#Name of Fishnet
outFeatureClass = "Coding_Challenge_SpermWhales.shp"
#Left Bottom Point of Data
originCoordinate = str(XMin) + " " + str(YMin)
#Y axis orientation
yAxisCoordinate = str(XMin) + " " + str(YMin + 1.0)
cellSizeWidth = "0.25"
cellSizeHeight = "0.25"
numRows =  ""
numColumns = ""
oppositeCorner = str(XMax) + " " + str(YMax)  # i.e. max x and max y coordinate
labels = "NO_LABELS"
templateExtent = "#"  #
geometryType = "POLYGON"  #
#create the fishnet
arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)
#check to see if this was successful
if arcpy.Exists(outFeatureClass):
    print("Created Fishnet file successfully!")

print("starting spatial join")
#Join the fishnet to observed points
target_features="Coding_Challenge_SpermWhales.shp"
join_features="SpermWhales_Output.shp"
out_feature_class="SpermWhales_HeatMap.shp"
join_operation="JOIN_ONE_TO_ONE"
join_type="KEEP_ALL"
field_mapping=""
match_option="INTERSECT"
search_radius=""
distance_field_name=""

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)
#check to see if completed
print("completed spatial join")

#Check that the heatmap is created and delete the intermediate files
if arcpy.Exists(out_feature_class):
    print("Created Heatmap file successfully!")
    print("Deleting intermediate files")
    arcpy.Delete_management(target_features)
    arcpy.Delete_management(join_features)



print("starting species two")

# 1. Convert Step_3_Cepphus_grylle.csv to a shapefile.
arcpy.env.workspace = r"C:\Data\d1\5\ALL_FILES"
in_Table1 = r"RightWhales.csv"
x_coords1 = "decimalLatitude"
y_coords1 = "decimalLongitude"
out_Layer1 = "RightWhales"
saved_Layer1 = r"RightWhales_Output.shp"

spRef1 = arcpy.SpatialReference(4326)  # 4326 == WGS 1984
lyr1 = arcpy.MakeXYEventLayer_management(in_Table1, x_coords1, y_coords1, out_Layer1, spRef1, "")

print(arcpy.GetCount_management(out_Layer1))
# Save to a layer file
arcpy.CopyFeatures_management(lyr1, saved_Layer1)
if arcpy.Exists(saved_Layer1):
    print("Created file successfully!")
# 2. Extact the Extent, i.e. XMin, XMax, YMin, YMax of the generated Cepphus_grylle shapefile.
desc1 = arcpy.Describe(saved_Layer1)
XMin1 = desc1.extent.XMin
XMax1 = desc1.extent.XMax
YMin1 = desc1.extent.YMin
YMax1 = desc1.extent.YMax
# 3. Generate a fishnet, but this time define the originCoordinate, yAxisCoordinate and oppositeCorner
# using the extracted extent from above. Hint: Formatting of the coordinate is important when generating
# the Fishnet, you must present it as: "-176.87 -41", note the space inbetween, and the fact that the
# entire thing is a string. Hint use: cellSizes of 0.25 degrees.

arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

outFeatureClass1 = "Coding_Challenge_RightWhales.shp"  # Name of output fishnet

originCoordinate1 = str(XMin1) + " " + str(YMin1)  # Left bottom of our point data
yAxisCoordinate1 = str(XMin1) + " " + str(YMin1 + 1.0)  # This sets the orientation on the y-axis, so we head north
cellSizeWidth1 = "0.25"
cellSizeHeight1 = "0.25"
numRows1 =  ""  # Leave blank, as we have set cellSize
numColumns1 = "" # Leave blank, as we have set cellSize
oppositeCorner1 = str(XMax1) + " " + str(YMax1)  # i.e. max x and max y coordinate
labels1 = "NO_LABELS"
templateExtent1 = "#"  # No need to use, as we have set yAxisCoordinate and oppositeCorner
geometryType1 = "POLYGON"  # Create a polygon, could be POLYLINE

arcpy.CreateFishnet_management(outFeatureClass1, originCoordinate1, yAxisCoordinate1,
                               cellSizeWidth1, cellSizeHeight1, numRows1, numColumns1,
                               oppositeCorner1, labels1, templateExtent1, geometryType1)

if arcpy.Exists(outFeatureClass1):
    print("Created Fishnet file successfully!")


# 4. Undertake a Spatial Join to join the fishnet to the observed points.
target_features1="Coding_Challenge_RightWhales.shp"
join_features1="RightWhales_Output.shp"
out_feature_class1="RightWhales_HeatMap.shp"
join_operation1="JOIN_ONE_TO_ONE"
join_type1="KEEP_ALL"
field_mapping1=""
match_option1="INTERSECT"
search_radius1=""
distance_field_name1=""

arcpy.SpatialJoin_analysis(target_features1, join_features1, out_feature_class1,
                           join_operation1, join_type1, field_mapping1, match_option1,
                           search_radius1, distance_field_name1)
# 5. Check that the heatmap is created and delete the intermediate files (e.g. species shapefile and fishnet). Hint:
# arcpy.Delete_management()..
if arcpy.Exists(out_feature_class1):
    print("Created Heatmap file successfully!")
    print("Deleting intermediate files")
    arcpy.Delete_management(target_features1)
    arcpy.Delete_management(join_features1)







# 6. Visualize in ArcGIS Pro
# Hint: To stop your script failing due to unable to overwriteOutput error, use the overwriteOutput environment setting:
import arcpy
arcpy.env.overwriteOutput = True  # If you get "already exists error" even when True, ensure file is not open in
# ArcGIS Pro or an other program such as Excel.


