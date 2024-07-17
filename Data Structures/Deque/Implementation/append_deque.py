from collections import deque


#create deque
de = deque([1,2,3])


print("Original Deque: ",de)


#append() : this function append values in last of the deque
de.append(4)
de.append(5)
print("Deque after appending right: ",de)


#appendleft() : this function append values in left of the deque
de.appendleft(0)
de.appendleft(-1)
print("Deque after appending left: ",de)