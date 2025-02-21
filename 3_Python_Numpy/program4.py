import numpy as np

arr = np.arange(11, 21)
print(arr)

# mean()
mean_result = np.mean(arr)
print(mean_result)

# std()
std_result = np.std(arr)
print(std_result)

# var()
var_result = np.var(arr)
print(var_result)

# median
median_result = np.median(arr)
print(median_result)

# sqrt
sqrt_result = np.sqrt(16)
print(sqrt_result)

# log()
log_result = np.log(10)
print(log_result)

# sin()
sin_result = np.sin(90)
print(sin_result)

# sum()
sum_result = np.sum(arr)
print(sum_result)

# max()
max_result = np.max(arr)
print(max_result)

# min()
min_result = np.min(arr)
print(min_result)

# argmax()-It returns the index value of the max element
arg_result = np.argmax(arr)
print(arg_result)

arg_min = np.argmin(arr)
print(arg_min)

# where()
where_result = np.where(arr>15, "apple", arr)
print(where_result)

# dtype
type_result = arr.dtype
print(type_result)

# creating new array
arr2 = np.random.randint(21, 32, size=(3,4))
print(arr2)

# checking dtype
type_result = arr2.dtype
print(type_result)

#random.seed()- It controls the randomness 
result = np.random.seed(45)
print(result)

# split
# In this method we only can create equal size array like arr having 10 items inside, so we can create 2 arrays
# of same size which means 5
new_arr = np.split(arr, 2)
print(new_arr)

new_arr = np.split(arr, 5)
print(new_arr)

# sort()
sort_result = np.sort(arr)
print(sort_result)

# copy()
copyArray = np.copy(arr)
print(copyArray)
print(copyArray + 5)

# round()
pi = np.round(3.14151617, 2)
print(pi)