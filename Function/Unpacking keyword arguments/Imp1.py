# Unpacking keyword arguments
#**kwargs keyword arguments can be unpacked using ** operator works as a dictionary
def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)  #output: {'name': 'Bob', 'age': 25}