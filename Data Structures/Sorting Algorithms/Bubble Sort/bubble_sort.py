def bubble_sort(li):
    n = len(li)
    for i in range(n):
        #this loop will start from 0 and go till n-i-1 which means it will go till the last element of the unsorted array
        for j in range(n-i-1):
            if li[j] > li[j+1]:
                '''If current element li[j] greater than next element li[j+1]
                then current element will be swapped with next element li[j] = li[j+1]
                and next element will be swapped with current element li[j+1] = li[j]
                denoted by li[j], li[j+1] = li[j+1], li[j]'''
                li[j], li[j+1] = li[j+1], li[j]
    return li

#defining list
li = [9,1,6,2,8,4,3]

#calling function
result = bubble_sort(li)
print(result)



