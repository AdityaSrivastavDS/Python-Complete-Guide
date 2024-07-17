from queue import Queue

# Create a new queue
q = Queue()


# Add some items to the queue
q.put(1)
q.put(2)
q.put(3)

# Remove an item from the queue
print(q.get())  # Output: 1


# Check if the queue is empty
print(q.empty())  # Output: False

# Get the size of the queue
print(q.qsize())  # Output: 2


print(q)