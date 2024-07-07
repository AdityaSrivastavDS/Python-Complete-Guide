#importing deque from collections module
from collections import deque

#declaing empty deque
stack = deque()

#adding elements in stack using append() method
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')

print("Original Stack: ", stack)

print()

#removing elements from stack using pop() method
#The pop() method will start removing elements from the last element of the list
print("Elements poped from stack: ")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())