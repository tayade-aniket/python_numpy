# NumPy Sorting Arrays
# We can use a simple np.sort() method for sorting Python NumPy arrays.

import numpy as np

# set alias names for dtypes
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]

# Values to be put in array
values = [
    ('Naruto', 2010, 6.9), 
    ('Sasuke', 2010, 8.2),
    ('Sakura', 2010, 7.8),
    ('Kakshi', 2001, 9.5)
    ]

# creating array
arr = np.array(values, dtype=dtypes)
print("\n Array Sorted by Name : \n", np.sort(arr, order='name'))
print("Array Sorted by Graduation Year and CGPA : \n", np.sort(arr, order=['grad_year', 'cgpa']))