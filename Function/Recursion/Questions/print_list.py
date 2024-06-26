#write a recursive function to print all elements of a list(Hint: use index and list as parameter)

#defining funcion
def print_list(list,idx = 0):
    #base case
    if(idx == len(list)):
        return
    print(list[idx]) #printing element at index idx
    print_list(list, idx+1) #calling function recursively with index incremented by 1
    

#defining list
list=["Aditya","Rahul","Rohit","Rajat","Rajesh"]

#calling function
print_list(list) 