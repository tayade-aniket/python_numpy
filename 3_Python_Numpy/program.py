# Creating a Numpy Array
# Arrays in Numpy can be created by multiple ways, with various number of Ranks, defining the size of the Array. 
# Arrays can also be created with the use of various data types such as lists, tuples, etc. 
# The type of the resultant array is deduced from the type of the elements in the sequences.


# importing library
import numpy as np

# creating one dimentional array
arr = np.array([10, 20, 30])
print("One Dimentional Array :", arr)

# To check it's dimention use following command
result = arr.ndim
print("Result of ndim :", result)

# creating two dimentional Array (dataset)
arr2 = np.array([[100, 200, 300], [400, 500, 600]])

print("Two Dimentional Array :", arr2)
result = arr2.ndim
print("Result of ndim :", result)

# Creating Three Dimentional Array
arr3 = np.array([[[111, 222, 333], [444, 555, 666], [777, 888, 999]]])

print("Three Dimentional Array :",arr3)
result = arr3.ndim
print("Result of ndim :", result)

# creating array from tuple
arr4 = np.array((22, 33, 44, 55, 66))
print("Array from tuple is :", arr4)

# to check shape of the array using 'shape'
print("Shape of arr :",arr.shape)
print("Shape of arr2 :",arr2.shape)
print("Shape of arr3 :",arr3.shape)
print("Shape of arr4 :",arr4.shape)

# creating array from 'arange'
arr5 = np.arange(1,8)
print("Array created using 'arange' :",arr5)

# passing only one value
arr6 = np.arange(7)
print("Array created using 'arange' using only one value :",arr6)

# creating array using floating number steps in range   
arr7 = np.arange(1, 10, 1.5)
# Printing array using for loop
for i in arr7:
    print(i)

# creating random dataset using 'np.random.randint'
arr8 = np.random.randint(12, 18, size=(3,4))
print("Random Dataset :\n",arr8)


