def add(x, y):
    return x + y

nums = [2, 3]

#*nums will unpack the list and pass it as arguments to the function
print(add(*nums))  #output: 5