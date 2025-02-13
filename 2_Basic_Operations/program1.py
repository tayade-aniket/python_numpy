# NumPy Basic Operations

# Element-wise operations in NumPy allow you to perform mathematical operations on each element of an 
# array individually, without the need for explicit loops.

# Element-wise Operations: We can perform arithmetic operations like addition, subtraction, multiplication, 
# and division directly on NumPy arrays.

import numpy as np

x = np.array([1,2,3])
y = np.array([4,5,6])

# Addition
add = x + y
print("Addition : ", add)

# Substraction
sub = x - y
print("Substraction : ", sub)

# Multiplication
product = x * y
print("Multiplication : ", product)

# Division
div = x / y
print("Division : ", div)