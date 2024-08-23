#Write a function sum_of_digits(num) that takes an integer and returns the sum of its digits.

def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num%10
        num = num//10
    return sum

#taking input from user
num = int(input("Enter a digit: "))

#calling function and storing result in a variable
result = sum_of_digits(num)
print(result)