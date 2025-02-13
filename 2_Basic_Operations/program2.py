# Unary Operation: These operations are applied to each individual element in the array, without the 
# need for multiple arrays (as in binary operations).

import numpy as np

# array with both positive and negative values
arr = np.array([-3, -1, 0, 1, 3])

# Applying a unary operation: absolute value
result = np.absolute(arr)
print("Absolute Values : ", result)

# Binary Operators: Numpy Binary Operations apply to the array elementwise and a new array is created. We can 
# use all basic arithmetic operators like +, -, /,  etc. In the case of +=, -=, = operators, the existing array 
# is modified.

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Applying a binary operation: addition
result = np.add(arr1, arr2)

print("Array 1 : ", arr1)
print("Array 2 : ", arr2)
print("Addition Result : ", result)
