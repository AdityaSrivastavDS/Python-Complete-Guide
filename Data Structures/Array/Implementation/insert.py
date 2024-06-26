from array import *

arr = array('i', [6,8,9,12])

print("Original array:")
for i in arr:
    print(i)

print()


#inserting new element in array using insert() method which takes two parameters: index and value
arr.insert(2,22)

print("Array after inserting new element:")
for i in arr:
    print(i)