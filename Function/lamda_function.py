#lamda function is a small anonymous function which can take any number of arguments, but can only have one expression.
#we had not used any return statement in lambda function, it always contains an expression which is returned.
lambda x, y: x + y
# lambda is a keyword
print((lambda x, y: x + y)(5, 3))  # 8



#using lamda functin with a variable
add = lambda x, y: x + y
print(add(5, 3))  # 8
