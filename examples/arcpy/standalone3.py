import arcpy
import glob
import os
import shutil

def cleanupFiles():
    # First get rid of modified files
    for l in ["l1","l2","l3"]:
    	arcpy.Delete_management(l)
    
    for f in glob.glob("C:\\Arctmp\\*"):
        try:
            shutil.rmtree(f)
        except:
            print "UNABLE TO REMOVE:",f
    # Now remove the old directory
    for i in xrange(0,1000000):
        new_workspace = "C:\\Arctmp\\workspace." + str(i)
        if not os.path.exists(new_workspace):
            break             
    print "TESTING USING WORKSPACE",new_workspace
    # Now move in fresh copies
    shutil.copytree("C:\\Arcbase",new_workspace)
    print "CONTENTS:"
    arcpy.env.workspace = new_workspace
    for f in sorted(glob.glob(arcpy.env.workspace + "\\*.shp")):
        print f
    for f in sorted(glob.glob(arcpy.env.workspace + "\\*.lyr")):
        print f
    for f in sorted(glob.glob(arcpy.env.workspace + "\\*.gdb")):
        print f

def report():
    print arcpy.GetMessages()

cleanupFiles()
    
shapefilelist0 = sorted(glob.glob(arcpy.env.workspace + "\*.shp"))                   # STEP 0
#[
shapefile0 = shapefilelist0 [0]                                                      # STEP 1
newlayer0 = "l1"                                                                     # STEP 2
#  or newlayer0 = "l2" 
#  or newlayer0 = "l3" 
#  swaps with step 3
#] (steps in [] can be in any order)
#[
featureclass0 = shapefile0                                                           # STEP 3
#  swaps with step 2
classorlayer0 = newlayer0                                                            # STEP 4
#  swaps with steps 10 11 12
fieldtype0 = "DATE"                                                                  # STEP 5
#  or fieldtype0 = "TEXT" 
#  or fieldtype0 = "FLOAT" 
#  or fieldtype0 = "DOUBLE" 
#  or fieldtype0 = "SHORT" 
#  or fieldtype0 = "LONG" 
#  swaps with steps 10 11 12
fieldname0 = "newf1"                                                                 # STEP 6
#  swaps with steps 10 11 12
op0 = ">"                                                                            # STEP 7
#  or op0 = "<" 
#  or op0 = "<=" 
#  or op0 = ">=" 
#  or op0 = "=" 
#  swaps with steps 10 11 12 14
val0 = "100"                                                                         # STEP 8
#  or val0 = "1000" 
#  swaps with steps 10 11 12 14
stattable0 = arcpy.env.workspace + "\stats.dbf"                                      # STEP 9
#  swaps with steps 10 11 12 14
#] (steps in [] can be in any order)
#[
fieldlist0 = arcpy.ListFields(featureclass0)                                         # STEP 10
#  swaps with steps 4 5 6 7 8 9 14
stattype0 = "FIRST"                                                                  # STEP 11
#  or stattype0 = "LAST" 
#  swaps with steps 4 5 6 7 8 9
statfields0 = []                                                                     # STEP 12
#  swaps with steps 4 5 6 7 8 9
#] (steps in [] can be in any order)
#[
statfields0.append([fieldname0,stattype0])                                           # STEP 13
print "STATFIELDS0=",statfields0
arcpy.AddField_management(featureclass0,fieldname0,fieldtype0); report()             # STEP 14
#  swaps with steps 7 8 9 10
#] (steps in [] can be in any order)
fieldname0 = fieldlist0 [0].name # STEP 15
print "FIELDNAME0=",fieldname0
print "OP0=",op0
print "VAL0=",val0
arcpy.MakeFeatureLayer_management(featureclass0,newlayer0,where_clause=' "' + fieldname0 + '" ' + op0 + val0); report()   # STEP 16
fieldname0 = "newf1"                                                                 # STEP 17
arcpy.DeleteField_management(featureclass0,fieldname0); report()                     # STEP 18
arcpy.Statistics_analysis(classorlayer0,stattable0,statfields0); report() # STEP 19

print 'TEST SUCCESSFULLY COMPLETED'
