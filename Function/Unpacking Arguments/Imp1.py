#*args positional arguments can be unpacked using * operator works as a tuple
def multiply(*args):
    print(args)
    total = 0
    for arg in args:
        total += arg
    return total

#here we had passed multiple arguments for function but still it will be treated as tuple
print(multiply(1, 2, 3, 4))

#output:
#(1, 2, 3, 4)
#10