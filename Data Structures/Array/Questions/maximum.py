#program to find the maximum element in a array

from array import *


#creating function to find maximum element
def max_element(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

#creating array
arr = array('i', [9,2,5,1,7,3])


#storing final result
result = max_element(arr)


#printing result
print("The maximum element of array is: ",result)
