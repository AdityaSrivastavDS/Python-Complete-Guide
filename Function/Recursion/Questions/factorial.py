#write a RECURSIVE function to calculate the factorial of a number.


#defining function 
def fact(n):
    #when n is 0 or 1, return 1 which means factorial of 0 and 1 is 1
    if(n == 0 or n == 1):
        return 1
    #fact(n-1) * n means (n-1) * (n-2) * (n-3) * ... * 1 * n
    return fact(n-1) * n  #fact(n-1) will call the function again and again until n becomes 1
    
#calling function
print(fact(5))  #120