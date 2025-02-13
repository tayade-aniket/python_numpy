# NumPy ufuncs
# NumPy provides familiar mathematical functions such as sin, cos, exp, etc. These functions also operate 
# elementwise on an array, producing an array as output.

import numpy as np

# create an array of Sine values
a = np.array([0, np.pi, np.pi/2])
print("All sine vlaues are : ", a)

# exponential values
a = np.array([0, 1, 2, 3, 4])
print("Exponent of Array Elements : ", np.exp(a))

# square root of array values
a = [4, 9, 16, 25]
print("Square root of Array Element are : ", np.sqrt(a))




# Explaination

# np.exp(x) calculates the exponential of each element in the array.
# It computes 
# 𝑒 to the power 𝑥 for each x in the array, where e is Euler's number (≈2.718).
