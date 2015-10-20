shapefilelist0 = sorted(glob.glob(arcpy.env.workspace + "\*.shp"))                   # STEP 0
shapefile0 = shapefilelist0 [0]                                                      # STEP 1
featureclass0 = shapefile0                                                           # STEP 2
#[
classorlayer0 = featureclass0                                                        # STEP 3
fieldtype0 = "DOUBLE"                                                                # STEP 4
#  or fieldtype0 = "TEXT"
#  or fieldtype0 = "FLOAT"
#  or fieldtype0 = "SHORT"
#  or fieldtype0 = "LONG"
#  or fieldtype0 = "DATE"
#  swaps with step 6
fieldname0 = "newf1"                                                                 # STEP 5
#  or fieldname0 = "newf3"
#  swaps with steps 6 8
#] (steps in [] can be in any order)
#[
insertcursor0 = arcpy.InsertCursor(classorlayer0)                                    # STEP 6
#  swaps with steps 4 5
arcpy.AddField_management(featureclass0,fieldname0,fieldtype0); report()             # STEP 7
#] (steps in [] can be in any order)
fieldname0 = "newf2"                                                                 # STEP 8
#  or fieldname0 = "newf3"
#  swaps with step 5
arcpy.AddField_management(featureclass0,fieldname0,fieldtype0); report()             # STEP 9
insertcursor0 = arcpy.InsertCursor(classorlayer0)                                    # STEP 10
