#implementation of stack using custom class with Linked list

#creating a class Node
class Node:
    #constructor to initialize value and next
    #next is a pointer to next node
    def __init__(self, value):
        self.value = value
        self.next = next

#creating a class Stack
class Stack:
    #constructor to initialize top
    #top is a pointer to top node of stack
    def __init__(self):
       self.top = None
    
    #method to push elements into stack
    def push(self, value):
        #creating a new node
        new_node = Node(value)
        #pointing new node to top
        new_node.next = self.top
        #making new node as top
        self.top = new_node

    #method to pop elements from stack
    def pop(self):
        #checking if stack is empty
        if self.top is None:
            raise IndexError("Poping from empty stack")
        #getting value of top node
        value = self.top.value
        #moving top
        self.top = self.top.next
        return value
    
    #method to display stack
    def display(self):
        #checking if stack is empty
        current = self.top
        #creating a list to store elements of stack
        elements = []
        #iterating through stack
        while current:
            elements.append(current.value)
            current = current.next
        return elements

    

#creating object of class Stack
stack = Stack()

#pushing elements into stack
stack.push(1)
stack.push(2)
stack.push(3)

print("Original Stack: ", stack.display())

print()

#poping elements from stack
print("Elements poped from stack: ")
print(stack.pop())
print(stack.pop())
print(stack.pop())
