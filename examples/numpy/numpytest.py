import numpy as np

dim0 = 1                                                                             # STEP 0
#  or dim0 = 10 
shape0 = (dim0)                                                                      # STEP 1
#  or shape0 = (dim0, dim0) 
#  or shape0 = (dim0, dim0, dim0) 
array0 = np.ones(shape0)                                                             # STEP 2
array0 = array0 + array0                                                             # STEP 3
array0 = array0 + array0                                                             # STEP 4
#  or array0 = array0 * array0 
array0 = array0 * array0                                                             # STEP 5
array0 = array0 * array0                                                             # STEP 6
array0 = array0 * array0                                                             # STEP 7
array0 = array0 * array0                                                             # STEP 8
array0 = array0 * array0                                                             # STEP 9
array0 = array0 * array0                                                             # STEP 10
array0 = array0 * array0                                                             # STEP 11
array0 = array0 * array0                                                             # STEP 12
array0 = array0 * array0                                                             # STEP 13
array0 = array0 - array0                                                             # STEP 14
#  or array1 = array0 - array0 
#  or array2 = array0 - array0 
#  or array3 = array0 - array0 
#  or array4 = array0 - array0 
#  or array5 = array0 - array0 
assert (np.array_equal(array0,array0))
