# Step 3 - Python Script from Tools

import os, arcpy
from arcpy.sa import *
listMonths = ["02", "04", "05", "07", "10", "11"]
outputDirectory = "C:/data/d1/6/ALL_Files/Step_3_data_lfs/NVDI"
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

for month in listMonths:
    arcpy.env.workspace = r"C:\data\d1\6\All_Files\Step_3_data_lfs\2015" + month
    listRasters = arcpy.ListRasters("*", "TIF")
    visRaster = [x for x in listRasters if ("T1_B4") in x]
    print("For vistion Rasters in month: " + month + ", there are: " + str(len(visRaster)) + " bands to process.")
    nirRaster = [x for x in listRasters if ("T1_B5") in x]
    print("For NIR Rasters in month: " + month + ", there are: " + str(len(nirRaster)) + " bands to process.")
    output_raster = "NVDI"+month
    output_raster = (Raster(nirRaster[0]) - Raster(visRaster[0])) / (Raster(nirRaster[0]) + Raster(visRaster[0]))
    output_raster.save(os.path.join(outputDirectory, "2015_" + month + "_NVDI.tif"))
   

