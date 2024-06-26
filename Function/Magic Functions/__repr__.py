class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # __repr__ method is called when we use repr() function
    # __repr__ method should return a string
    #this functions is used to print the object in a more detailed way
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"

bob = Person("Bob", 21)
print(bob)