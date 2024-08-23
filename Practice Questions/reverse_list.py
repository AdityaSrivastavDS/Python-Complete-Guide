#Write a function reverse_list(lst) that reverses a given list.

def revrse_list(lst):
    lst.reverse()
    return lst

#taking input from user
lst = []
n = int(input("Enter number of elements: "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)

#calling function and storing result in a variable
result = revrse_list(lst)
print(result)