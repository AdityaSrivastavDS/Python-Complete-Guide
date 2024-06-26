from array import *


arr = array('i', [98,34,56,71,24])

print("Original array:")
for i in arr:
    print(i)

print()


#deleting element from array using remove() method which takes one parameter: value
arr.remove(71)


print("Array after deleting element:")
for i in arr:
    print(i)