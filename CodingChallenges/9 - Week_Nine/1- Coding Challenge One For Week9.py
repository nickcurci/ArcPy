# Coding Challenge 9
import arcpy
import time

####################
###set output dir###
###set input shp ###
####################
input_shp =r'C:\data\d1\9\forest\RI_Invasives\RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp'
output = r'C:\data\d1\9\forest\output'

print("This challenge uses the RI invasive species dataset")
time.sleep(3)
print("First we wil count how many sites have photos, and how many do not (2 numbers), print the results.")
time.sleep(1)
print("running")
arcpy.env.overwriteOutput = True
fields = ['Point_num', 'site', 'photo']

expression = arcpy.AddFieldDelimiters(input_shp, "photo") + " LIKE 'y'"
expression1 = arcpy.AddFieldDelimiters(input_shp, "photo") + " NOT LIKE 'y'"
count = 0
count1 = 0
with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        count = count + 1
with arcpy.da.SearchCursor(input_shp, fields, expression1) as cursor:
    for row in cursor:
        count1 = count1 + 1
print("There are ", count, " sites with photos")
print("There are ", count1, " sites with no photos")
time.sleep(3)

print("Next we will count how many unique species there are in the dataset, print the result.")
time.sleep(1)
table = input_shp
field = "Species"
def unique_values(table , field):
    with arcpy.da.SearchCursor(table, field) as cursor:
        return sorted({row[0] for row in cursor})
specieslist = unique_values(input_shp , field)
print ("The unique species names are: ", specieslist)

time.sleep(3)
print("Now we will generate two shapefiles, one with photos and the other without.")
time.sleep(1)
print("running select for photos")
invasive_photos = arcpy.SelectLayerByAttribute_management(input_shp,"NEW_SELECTION",""""photo" LIKE 'y' """)
arcpy.CopyFeatures_management(invasive_photos, output + '\Invasives_with_photos.shp')
time.sleep(1)
print("running select for no photos")
invasive_no_photos = arcpy.SelectLayerByAttribute_management(input_shp,"NEW_SELECTION",""""photo" NOT LIKE 'y' """)
arcpy.CopyFeatures_management(invasive_no_photos, output + '\Invasives_with__no_photos.shp')
print("done, view your shapefiles in the output directory")
