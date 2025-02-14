# Basic Array Operations
# In numpy, arrays allow a wide range of operations which can be performed on a particular array or a combination 
# of Arrays. These operation include some basic Mathematical operation as well as Unary and Binary operations.

# impoting numpy library
import numpy as np

# Defining  Array 1
arr1 = np.array(
    [
        [1000, 2000],
        [3000, 4000]
    ]
)

# Defining  Array 2
arr2 = np.array(
    [
        [99, 88],
        [77, 66]
    ]
)

# Adding 1 to every element
print("Adding 1 to every element :", arr1 + 1)

# Subtracting 2 from each element
print("Substracting 2 from each element :",arr2 - 2)

# Performing Unary operations
print("Sum of all Elements using Unary Operation :", arr1.sum())

# Performing Binary operations
print("Sum of Elements using Binary Operations :", arr1 + arr2)