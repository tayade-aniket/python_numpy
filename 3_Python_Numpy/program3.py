import numpy as np

arr = np.arange(11, 21)
print(arr)

arr2 = np.random.randint(21,45, size=(4,5))
print(arr2)

# Performaing artithmatic Operations with arr
print(arr + 5)
print(arr + arr)
print(arr * 2)
print(arr ** 2)

# Performing comparison operations with arr
print(arr > 14)         # this will only print the result
print(arr[arr > 14])    # This will print values which pass the test

# creating new array with previous one
arr3 = arr2[arr2 > 30]
print(arr3)

print("Array 2 Dimention",arr2.ndim)
print("Array 3 Dimention",arr3.ndim)