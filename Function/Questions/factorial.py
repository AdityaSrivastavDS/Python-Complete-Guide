#write a function to calculate the factorial of a number n

#defining function
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

#calling function
n = 4
result = factorial(n)

print("Factorial of", n , "is", result)