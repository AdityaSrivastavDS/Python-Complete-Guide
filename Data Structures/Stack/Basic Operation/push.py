class Stack:
    def __init__(self):
        self.stack = []

    def add(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    
    #Use peek to look at the top of the stack
    def peek(self):
        return self.stack[-1]
    
    #display elements of stack
    def display(self):
        for i in self.stack:
            print(i)
    

#creating object of Stack Class
stack = Stack()

#adding and removing elements in stack
stack.add(1)
stack.add(2)
stack.add('Monday')
stack.add("Mon")
stack.add("Tue")
stack.peek()
print(stack.peek())
stack.add("Wed")
stack.add("Thu")
print(stack.peek())