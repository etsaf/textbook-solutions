#from collections import deque
#stack = deque()
#stack.append('a')
#stack.append('b')
#print(stack.pop())
#print(stack.pop())
class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        if len(self.stack) >= 1:
            a, minim = self.stack.pop()
            if item < minim:
                self.stack.append((a, minim))
                self.stack.append((item, item))
            else:
                self.stack.append((a, minim))
                self.stack.append((item, minim))
        else:
            self.stack.append((item, item))

    def size(self):
        return len(self.stack)
    
    def minimum(self):
        a, minim = self.stack.pop()
        self.stack.append((a, minim))
        return minim

# And a queue that only has enqueue and dequeue operations
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)
    
stack = Stack()
stack.push(8)
stack.push(6)
stack.push(3)
stack.push(7)
print(stack.minimum())