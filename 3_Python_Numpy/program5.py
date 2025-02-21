import numpy as np

# creating new array
arr = np.random.randint(21, 32, size=(4,5))
print(arr)

# vstack-vertical stacking.One arrays comes below another array.No of rows get increased.But no of columns remain same. 
#  To do the vstack all arrays must have same no of columns.

v_stack = np.vstack([arr, arr])
print("\n V Stack Array : \n", v_stack)

# hstack-horizontal stacking.In hstack onr array comes beside another array.No of columns get increased.
# But no of rows # ramin same. To do the hstack we must same no of rows with all arrays.
h_stack = np.hstack([arr, arr])
print("\n H Stack Array : \n", h_stack)


# concatenate 
# row wise concatenation-axis=0.One array comes below another array.No of rows gets increased but no of columns remain same. 
# To do row wise concatenate we must have same no of columns.
row_wise_concat = np.concatenate([arr, arr], axis=0)
print("\n Row Wise Concat : \n", row_wise_concat)


# col wise concatenate- axis=1. One array comes beside another array.No of columns get increased but no of rows remain same. 
# To do col wise concatenate we must have same no of rows.
col_wise_concat = np.concatenate([arr, arr], axis=1)
print("\n Column Wise Concat : \n", col_wise_concat)

# reshape

# first perform shape
print(col_wise_concat.shape)

# explaination- 1 x 40 = 40
#               2 x 20 = 40
#               4 x 10 = 40
#               5 x 8  = 40

# check ndim
print(col_wise_concat.ndim)

new_result = np.reshape(arr, (5, 4))
print(new_result)

new_arr = np.array([11, 32, 43, 54, 65, 76, 87, 98, 110])
print(new_arr)

# broadcasting 
new_arr[0:4]=50
print(new_arr)

new_arr[0:4]=[1998, 1988, 1978, 1968]
print(new_arr)

# we can pass multiple indexs and values like follow -
new_arr[[0, 2, 4, 6, 8]] = [2000, 2002, 2004, 2006, 2008]
print(new_arr)


# we also can use random method differently
normal_array = np.random.normal(0,1,5)
print(normal_array)

poisson_aaray = np.random.poisson(5, 10)
print(poisson_aaray)

bionomial_array = np.random.binomial(10, .5, 5)
print(bionomial_array)

# zeros
arr2 = np.zeros(5)
print(arr2)

# ones
arr3 = np.ones(5)
print(arr3)
