class Priority_Queue:
    #declaring empty queue
    def __init__(self):
        self.queue = []

    #inserting elements in the queue
    def enqueue(self, item, priority):
        self.queue.append((priority, item))
        self.queue.sort(reverse = True)  #higher priroity elements come first

    #removing elements from the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue.pop()[1]
    
    #checking if queue is empty
    def is_empty(self):
        return len(self.queue) == 0
    
    #displaying the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Elements in priority Queue are: ", end = " ")
            for item in self.queue:
                print(item[1], end = " ")
            print()


#Usage
pq = Priority_Queue()

#inserting elements in the queue
pq.enqueue("A", 3)
pq.enqueue("B", 2)
pq.enqueue("C", 1)

#displaying the queue
pq.display()

#removing elements from the queue
print("Removed element: ", pq.dequeue())
pq.display()