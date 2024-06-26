def add(x , y):
    return x + y

#defining dictionary as arguments
nums = {"x":12, "y":13}

#**nums will unpack the dictionary and pass it as arguments to the function
print(add(**nums))  #output: 25