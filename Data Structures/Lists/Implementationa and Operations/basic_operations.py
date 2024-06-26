# Example of basic list operations
my_list = [1, 2, 3, 4, 5]



# List methods

# append() method adds an element to the end of the list
my_list.append(6)
print(my_list)      # Output: [1, 2, 'three', 4, 5, 6]


# insert() method adds an element at the specified position
my_list.insert(2, 'three')
print(my_list)      # Output: [1, 2, 'three', 4, 5, 6]


# remove() method removes the first occurrence of the specified element
my_list.remove('three')
print(my_list)      # Output: [1, 2, 4, 5, 6]
