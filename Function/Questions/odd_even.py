#write  afunction that returns a string "odd" when a number is odd and "even" when a number is even

#defining function
def even_odd(num):
    if(num % 2 == 0):
        return "even"
    else:
        return "odd"


#taking input from user
num = int(input("Enter a number: "))

#calling function
print(even_odd(num))