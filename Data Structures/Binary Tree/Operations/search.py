class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data, end=' ')
        if self.right:
            self.right.PrintTree()

    
    def search(self, data):
        # Recursive function to search a value
        if self is None or self.data == data:
            return self

        # If the data to be found is smaller than the root's data, search in the left subtree
        if data < self.data:
            return self.left.search(data) if self.left else None
        
        # If the data to be found is greater than the root's data, search in the right subtree
        return self.right.search(data) if self.right else None

# Example usage:
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(8)
root.insert(13)
root.insert(15)

print("Tree before operations:")
root.PrintTree()

# Searching
search_value = 8
result = root.search(search_value)
print(f"\n\nSearching for {search_value}: {'Found' if result else 'Not Found'}")

search_value = 20
result = root.search(search_value)
print(f"Searching for {search_value}: {'Found' if result else 'Not Found'}")
