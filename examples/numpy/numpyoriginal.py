import numpy as np

dim2 = 1 
shape2 = (dim2, dim2) 
array5 = np.ones(shape2) 
array0 = np.ones(shape2) 
array1 = array5 + array0 
array2 = np.ravel(array1) 
array5 = array2 + array2 
array4 = array5 + array1 
array3 = array0 + array4 
array0 = array3 * array5 
array5 = array0 * array0 
array4 = array5 - array3 
array3 = array4 * array4 
np.copyto(array2,array3) 
array1 = array2 * array0 
array5 = array1 - array2 
np.copyto(array0,array2) 
array2 = array5 * array0 
array5 = array2 - array4 
array3 = array2 * array5 
array2 = array3 * array3 
array3 = array2 + array1 
array5 = array5 - array3 
array2 = array5 * array5 
array3 = array5 + array2 
array4 = array4 - array3 
array5 = array3 * array4 
array3 = array4 * array5 
array5 = np.zeros_like(array5) 
array5 = array5 * array3 
assert (np.array_equal(array5,array5))
