import numpy as np

dim1 = 1
shape2 = (dim1, dim1, dim1)
array1 = np.ones(shape2)
array0 = array1 * array1
array1 = array1 + array1
array4 = array0 + array1
array0 = np.reshape(array4,shape2)
array3 = array1 * array4
array2 = np.ravel(array4)
array5 = array2 - array3
array4 = array5 * array2
array1 = np.unique(array0)
array5 = array5 * array3
array0 = array1 * array5
array5 = np.unique(array0)
array1 = array4 - array2
array2 = array0.flatten()
array0 = array5 + array5
array5 = array5 + array2
array2 = array0 * array2
np.copyto(array5,array2)
array2 = array2 * array5
array3 = array0 * array2
array0 = array3 - array1
array4 = array3 * array0
array1 = array5 + array4
array5 = array0 * array1
array0 = array5 - array1
array4 = array0 * array3
array3 = array4 * array0
array1 = array5 + array3
array0 = array2 + array1
array5 = array5 - array0
array5 = array3 * array5
array0 = array1 + array5
array2 = array3 - array0
array4 = array2 * array1
array3 = array4 * array2
array2 = array0 - array0
np.copyto(array1,array3)
array4 = array2.flatten()
array1 = array1 * array4

print array1

assert (np.array_equal(array1,array1))
