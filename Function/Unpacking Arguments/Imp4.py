
def multiply(*args):
    total = 1
    for arg in args:
        total *= arg

    return total


#*args positional arguments can be unpacked using * operator works as a tuple
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)  # sum() is a built-in function that adds all the elements in a list
    else:
        return "No valid operator provided to apply()"
    

print(apply(1, 3, 6, 7, operator="+"))