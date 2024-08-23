#Ques: Swap two numbers without using a third variable


#taking user input
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))


print("Original Number: ", a, b)

#swapping numbers logic
a = a-b
b = b+a
a = b-a


print("Swapped Number: ", a, b)