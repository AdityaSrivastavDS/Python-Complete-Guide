# write a recursive funcion to calculate the sume of first n natural numbers

#defining function
def sum_num(n):
    if(n == 0):
        return 0 # if n is 0 then return 0
    # sum+_num(n-1) means it will call the function again with n-1
    return n + sum_num(n-1)

#printing final results
print(sum_num(9))