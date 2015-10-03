import arcpy
import sys

shapefile0 = sys.argv[1]                                                             # STEP 1
newlayer0 = "l1"                                                                     # STEP 2
featureclass0 = shapefile0                                                           # STEP 3
fieldname0 = "newf1"                                                                 # STEP 4
selectiontype0 = "SWITCH_SELECTION"                                                  # STEP 5
op0 = ">"                                                                            # STEP 6
val0 = "100"                                                                         # STEP 7
arcpy.MakeFeatureLayer_management(featureclass0, newlayer0)                          # STEP 8
arcpy.SelectLayerByAttribute_management(newlayer0,selectiontype0,' "' + fieldname0 + '" ' + op0 + val0)   # STEP 9
arcpy.Delete_management(featureclass0)                                               # STEP 10
arcpy.SelectLayerByAttribute_management(newlayer0,selectiontype0,' "' + fieldname0 + '" ' + op0 + val0)   # STEP 11
