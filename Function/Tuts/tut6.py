def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
print(doubled)

doubleds = map(double, sequence)
print(doubleds)


doubledss = list(map(lambda x: x * 2, sequence))
print(doubledss)