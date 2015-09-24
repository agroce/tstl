import shutil
import os
import glob
import arcpy
def cleanupFiles():
    for f in glob.glob("C:\\Arctmp\\*"):
        try:
            arcpy.Delete_management(f)
        except:
            print "UNABLE TO REMOVE:",f
            print arcpy.GetMessages()
    for f in glob.glob("C:\\Arcbase\\*"):
        shutil.copy(f, f.replace("Arcbase","Arctmp"))

cleanupFiles()

shapefilelist0 = glob.glob("C:\\Arctmp\\*.shp") 
shapefile0 = shapefilelist0 [0] 
featureclass0 = shapefile0; print "featureclass0 =",featureclass0 
shapefile0 = "C:\\arctmp\\new1.shp" 
newlayer0 = "l1" 
featureclass1 = shapefile0 
overlaptype0 = "COMPLETELY_CONTAINS" 
arcpy.CopyFeatures_management(featureclass0,featureclass1) 
arcpy.MakeFeatureLayer_management(featureclass1, newlayer0); print arcpy.GetMessages() 
arcpy.SelectLayerByLocation_management(newlayer0,overlaptype0,newlayer0); print arcpy.GetMessages()

cleanupFiles()
# Should delete all the data created so far

newlayer0 = "l1" 
overlaptype0 = "SHARE_A_LINE_SEGMENT_WITH"
print "arcpy crashes Python on the next call"
arcpy.SelectLayerByLocation_management(newlayer0,overlaptype0,newlayer0); print arcpy.GetMessages() 
print "TEST COMPLETED SUCCESSFULLY"
