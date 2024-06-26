# Description: Default parameter in function
#   - Default parameter is used when no argument is passed to the function


#multiple default parameter
def prod(a = 4, b = 6):
    return a * b

print(prod())



#single defualt parameter

def sum(a, b = 4):
    return a + b

print(sum(5)) #5 will be stored in a

'''
Default paramter should be at the end of the parameter list not at first or middle

wrong: def sum(a = 4, b):
wrong: def sum(a, b = 4, c):

right: def sum(a, b = 4):'''