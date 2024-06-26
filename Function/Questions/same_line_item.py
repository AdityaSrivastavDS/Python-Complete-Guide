#write a function that print all elements of a list on same line

#creating list
list = ["Aditya", "Mahir", "Rahul", "Rohit", "Raj", "Ravi", "Rahul", "Rohit", "Raj", "Ravi"]


#defining function
def print_elements(list):
    for item in list:
        print(list, end = " ")


#calling function
print_elements(list)