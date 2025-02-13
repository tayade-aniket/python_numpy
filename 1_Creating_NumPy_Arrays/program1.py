# importing library
import numpy as np

#creating 1D array
x = np.array([10, 20, 30])

# creating 2D array
y = np.array([[100, 200, 300, 400], [500, 600, 700, 800]])

# creating 3D array
z = np.array([[[1000, 2000, 3000], [4000, 5000, 6000], [7000, 8000, 9000]]])

# printing all our array
print(x)
print(y)
print(z)


# Using Numpy Functions: NumPy provides convenient methods to create arrays initialized with specific 
# values like zeros and ones:

a1_zeros = np.zeros((3,3))
a2_ones = np.ones((2,2))
a3_range = np.arange(0, 10, 2)

# printing 
print(a1_zeros)
print(a2_ones)
print(a3_range)