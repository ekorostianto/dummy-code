# Import system modules  
import arcpy  
from arcpy import env  
from arcpy.sa import *  
  
# Input data source  
arcpy.env.workspace = "D:/College/Semester7/KP_2020/Progress/sentinel5p/hasil/qa50/New_folder"
arcpy.env.overwriteOutput = True  
  
# Set output folder  
OutputFolder = "D:/College/Semester7/KP_2020/Progress/sentinel5p/hasil/qa50/New_folder"  
  
  
# Loop through a list of files in the workspace  
NCfiles = arcpy.ListFiles("*.nc")
  
for filename in NCfiles:  
    print("Processing: " + filename)  
    inNCfiles = arcpy.env.workspace + "/" + filename  
    fileroot = filename[0:(len(filename)-3)]  
    TempLayerFile = "Sentinel5PNO2L3_tropospheric_NO2_column_number_density"  
    outRaster = OutputFolder + "/" + fileroot  
  
    # Process: Make NetCDF Raster Layer  
    arcpy.MakeNetCDFRasterLayer_md(inNCfiles, "tropospheric_NO2_column_number_density", "longitude", "latitude", TempLayerFile, "", "", "BY_VALUE")  
  
    # Process: Copy Raster  
    arcpy.CopyRaster_management(TempLayerFile, outRaster + ".tif", "", "", "", "NONE", "NONE", "")  
     
  
print "***DONE!!!"  
print arcpy.GetMessages()