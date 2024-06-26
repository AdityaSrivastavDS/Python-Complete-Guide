class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__ method is called when we use print() function
    # __str__ method should return a string
    #It tells the print() function what to print when we print the object
    def __str__(self):
        return f"Person {self.name}, {self.age} years old"

bob = Person("Bob", 21)
print(bob)  # <__main__.Person object at 0x7f3e3c1e3f10> this output because we have not defined __str__ method