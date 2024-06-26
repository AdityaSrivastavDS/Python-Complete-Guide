#write a function to convert usd value into inr


#defining function
def converter(usd_value):
    inr_value = usd_value * 85.4  #1 USD = 85.4 INR
    return inr_value

#taking inpt from user
inr_value = int(input("Enter the USD value: ")).__round__(2)   #__round__() is used to round off the value to 2 decimal places


#calling function
print("The value of USD in INR is: ", converter(inr_value))