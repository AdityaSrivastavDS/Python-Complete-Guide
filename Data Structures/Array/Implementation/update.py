from array import *

arr = array('i', [45,67,87,34,21])

print("Original array:")
for i in arr:
    print(i)

print()


#updating element in array using index
arr[2] = 99


print("Array after updating element:")
for i in arr:
    print(i)