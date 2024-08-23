#Write a function count_vowels(s) that counts the number of vowels in a string.

def count_vowels(s):
    count = 0
    vowels = ['a','e','i','o','u']

    #checking for vowels
    for char in s:
        if char in vowels:
            count += 1
    return count

#taking input from user
s = input("Enter a string: ")

#calling function and storing result in a variable
result = count_vowels(s)
print(result)