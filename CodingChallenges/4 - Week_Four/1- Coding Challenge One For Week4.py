# Name: ExtractFeaturesByLocationAndAttribute.py
# Description: Extract features to a new feature class based on a spatial
# relationships to another layer, and an attribute query

# Import system modules
import arcpy

# Set the workspace
arcpy.env.workspace = 'c:/data/mexico.gdb'
# Select all cities that overlap the chihuahua polygon
chihuahua_cities = arcpy.SelectLayerByLocation_management('cities', 'INTERSECT',
                                                          'chihuahua', 0,
                                                          'NEW_SELECTION')

# Within selected features, further select only those cities with a
# population > 10,000
arcpy.SelectLayerByAttribute_management(chihuahua_cities, 'SUBSET_SELECTION',
                                        '"population" > 10000')

# Write the selected features to a new feature class
arcpy.CopyFeatures_management(chihuahua_cities, 'chihuahua_10000plus')
