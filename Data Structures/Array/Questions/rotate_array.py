#Rotate array upto certain number of given steps

#Time complexity: O(n)
#Space complexity: O(1)

#function to rotate array
def rotate_array(arr, k):
    #storing length of array
    n = len(arr)

    k = k%n #to handle cases where k > n

    if k == 0:
        return arr
    
    #reverse entire array
    reverse(arr, 0, n-1)

    #revserse first k elements
    reverse(arr, 0, k-1)

    #reverse the remaining elements
    reverse(arr, k, n-1)

    return arr

#function to reverse the array
def reverse(arr, start, end):
    #loop to reverse the array
    while start < end:
        #swapping elements
        arr[start], arr[end] = arr[end], arr[start]
        #incrementing start and decrementing end
        start +=1
        end -=1

#creating array
arr = [1,2,3,4,5,6,7]
steps = 3

#original array
print('Original array: ', arr)

print()

rotated_array = rotate_array(arr, steps)


#rotated array
print('Rotated array: ')
print(rotated_array)