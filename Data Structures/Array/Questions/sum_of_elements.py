#Write a function to calculate the sum of all the elements in an array.

from array import *

def sum_of_elements(arr):
    sum = 0
    for i in arr:
        sum+=i
    return sum
    
#creating array
arr = array('i', [1,2,3,4,5,6])

#creating variable to store final result
result = sum_of_elements(arr)

#printing result
print("The sum of all elements of array is: ",result)