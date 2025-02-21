# Slicing of Two Dimentional Array

import numpy as np

arr = np.array([
    [11, 34, 52, 67, 89],
    [41, 29, 44, 99, 61],
    [84, 56, 94, 73, 81]
])

# How slice two dimentional Array 
# row - 1st and 2nd
# coulmn - 2nd and 3rd
print(arr[1:3, 2:4])


arr2 = np.array([
    [65, 88, 86, 54, 60],       
    [73, 85, 70, 88, 52],       
    [63, 59, 80, 88, 64],       
    [54, 58, 72, 60, 88]
])

# row- 1st to 3rd row 
# col- 1st to 3rd col 
print(arr2[1:4, 1:4])

# row- 1st & 2nd row 
# col- 0th,1st & 2nd col 
print(arr2[1:3, 0:3])