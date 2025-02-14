import numpy as np

myList = [10, 20, 30, 40, 50]
# result = myList + 5
# print(result)       # TypeError: can only concatenate list (not "int") to list 

result = myList + myList
print(result)

result = myList * 3
print(result)       # It will print same list 3 times

arr = np.array([10,20,30], [40, 50, 60])
print(arr)          # TypeError: Field elements must be 2- or 3-tuples, got '40'
