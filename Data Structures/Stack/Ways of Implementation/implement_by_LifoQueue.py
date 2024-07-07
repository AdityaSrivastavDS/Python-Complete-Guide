#Implementation of Stack using LifoQueue

#Importing LifoQueue from queue module
from queue import LifoQueue

#creating object of LifoQueue
stack = LifoQueue()

#pushing elements into stack
stack.put(1)
stack.put(2)
stack.put(3)

#displaying stack
print("Original Stack: ", list(stack.queue))


#Pop elements from stack
print("Poped element: ")
print(stack.get())
print(stack.get())
print(stack.get())



#Time Complexity: O(1) for push(), pop() and display() methods.
#Space Complexity: O(n) where n is the number of elements in stack.


#LifoQueue is a class in queue module which is used to implement stack. It is a subclass of Queue class. It is a thread-safe class which means it can be used in multithreading. It has two methods put() and get() to push and pop elements from stack respectively. It has an attribute queue which is a deque object to store elements of stack.