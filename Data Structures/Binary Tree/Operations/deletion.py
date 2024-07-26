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

    def min_value_node(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def delete(self, data):
        # Recursive function to delete a node
        if self is None:
            return self

        # If the data to be deleted is smaller than the root's data, then it lies in the left subtree
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        # If the data to be deleted is greater than the root's data, then it lies in the right subtree
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        # If data is same as root's data, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if self.left is None:
                temp = self.right
                return temp
            elif self.right is None:
                temp = self.left
                return temp

            # Node with two children: Get the in-order successor (smallest in the right subtree)
            temp = self.right.min_value_node()

            # Copy the in-order successor's content to this node
            self.data = temp.data

            # Delete the in-order successor
            self.right = self.right.delete(temp.data)

        return self

# Example usage:
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(8)
root.insert(13)
root.insert(15)

print("Tree before deletion:")
root.PrintTree()

root.delete(6)
print("\nTree after deleting 6:")
root.PrintTree()

root.delete(14)
print("\nTree after deleting 14:")
root.PrintTree()

root.delete(12)
print("\nTree after deleting 12:")
root.PrintTree()
