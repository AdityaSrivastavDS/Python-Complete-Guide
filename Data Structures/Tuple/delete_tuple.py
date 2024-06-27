'''Tuple is immutable, so we can't delete elements from it. But we can delete the whole tuple using 
del keyword.'''


#creating tuple
t = (24, 45, 78, 98)
t1 = ("Adi", "Mahi", "Pihu")

#deleting tuple using del keyword
del t

print(t1)
print(t) #NameError: name 't' is not defined