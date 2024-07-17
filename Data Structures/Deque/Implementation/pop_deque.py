import collections


#create deque
dq = collections.deque([1,2,3,4,5,6])

print("Original Deque: ",dq)


#pop() : this function remove values from right of the deque
dq.pop()
print("Deque after popping right: ",dq)


#popleft() : this function remove values from left of the deque
dq.popleft()
print("Deque after popping left: ",dq)