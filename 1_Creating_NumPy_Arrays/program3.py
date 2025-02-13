# Slicing: Just like lists in Python, NumPy arrays can be sliced. As arrays can be multidimensional, 
# you need to specify a slice for each dimension of the array.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# element from index 1 to 3
print("Range of Elements : ", arr[1:4])

# printing all row second column
print("Multi-Dimetional Slicing : ", arr[:, 1])


# Advanced Indexing: Advanced Indexing in NumPy provides more powerful and flexible ways to access and 
# manipulate array elements.

arr1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# integer array indexing
indices = np.array([1, 3, 5])
print("Integer Array Indexing : ", arr1[indices])

# boolean array indexing
cond = arr1 > 50
print("\n Element greater than 50 are : \n", arr1[cond])