#write a recursive function that show numbers

#defining function
def show_num(n):
    if(n == 0):
        return 
    show_num(n-1)
    print(n)
#calling function
show_num(6)

print()

#function to print same numbers but in reverse order
#defining function
def show_num_rev(num):
    if(num == 0):
        return 
    print(num)  #to reverse we will print first then call the function
    show_num(num-1)
   
#calling function
show_num_rev(6)
