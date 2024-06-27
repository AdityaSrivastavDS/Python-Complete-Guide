#nested tuple can create a more complex data structure

#creating nested tuple
t = (24, 45, 78, 98, ("Adi", "Mahi", "Pihu"), (1, 2, 3))

print(t)

print()

#this will print every sub tuple separately
for i in t:
    print(i)