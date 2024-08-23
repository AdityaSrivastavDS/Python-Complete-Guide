#Ques: Write a program to extract the digit from a given number and print them in reverse order separated from each other.

#taking user input
num = int(input("Enter number for extraction: "))


#extracting digits from integer number
digits = []

while num > 0:
    digits.append(num%10)
    num = num//10

print(digits)