class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None  # Pointer to the front of the queue
        self.rear = None   # Pointer to the rear of the queue
        self.size = 0      # Current size of the queue

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            # If queue is empty, set both front and rear to the new node
            self.front = new_node
            self.rear = new_node
        else:
            # Add new node at the rear and update rear pointer
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        # Remove node from the front and update front pointer
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None  # If queue becomes empty, reset rear pointer
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    def is_empty(self):
        return self.front is None

    def size(self):
        return self.size


# Creating a linked list based queue
queue = LinkedListQueue()

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())  # Output: Queue size: 3

# Peek at the front element
print("Front element:", queue.peek())  # Output: Front element: 1

# Dequeue elements
print("Dequeue:", queue.dequeue())  # Output: Dequeue: 1
print("Dequeue:", queue.dequeue())  # Output: Dequeue: 2

print("Is queue empty?", queue.is_empty())  # Output: Is queue empty? False

# Enqueue more elements
queue.enqueue(4)
queue.enqueue(5)

# Dequeue remaining elements
while not queue.is_empty():
    print("Dequeue:", queue.dequeue())

# Output:
# Dequeue: 3
# Dequeue: 4
# Dequeue: 5

print("Is queue empty?", queue.is_empty())  # Output: Is queue empty? True
