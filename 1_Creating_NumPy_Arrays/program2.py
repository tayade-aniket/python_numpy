# NumPy Array Indexing
# Knowing the basics of NumPy array indexing is important for analyzing and manipulating the array object.
# Basic Indexing: Basic indexing in NumPy allows you to access elements of an array using indices.

import numpy as np

# crating 1D array
arr1 = np.array([10, 20, 30, 40, 50])

# single element accessing
print("Single Element Access : ", arr1[2])

# Negative indexing
print("Negative Indexing : ", arr1[-1])

# creating 2D array
arr2 = np.array([[100, 200, 300], [400, 500, 600], [700, 800, 900]])

# Multi-dimentional array accessing
print("Multi-Dimentional Array Accessing : ",arr2[1, 0])