from collections import deque
#stack = deque()
#stack.append('a')
#stack.append('b')
#print(stack.pop())
#print(stack.pop())
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

class Shelter:
    def __init__(self):
        self.queueDog = deque()
        self.queueCat = deque()
    def enqueue(self, item):
        new = item
        dog1, numD1 = self.queueDog.pop(0)
        cat1, numC1 = self.queueCat.pop(0)
        newnum = max(numD1, numC1) + 1
        if new in cat:
            self.queueCat.append(new, newnum)
        else:
            self.queueDog.append(new, newnum)        
    def dequeueDog(self):
        x, y = self.queueDog.pop(0)
        return x
    def dequeueCat(self):
        x, y = self.queueCat.pop(0)
        return x
    def dequeueAny(self):
        d, dog0 = self.queueDog.pop(0)
        c, cat0 = self.queueCat.pop(0)
        if dog0 > cat0:
            self.queueDog.append(d, dog0)
            return c
        else:
            self.queueCat.append(c, cat0)
            return d
stack = Stack()
stack.push(8)
stack.push(6)
stack.push(3)
stack.push(7)
stack.push(10)
stack.push(1)
ans = sortStack(stack)
while ans.size() != 0:
    print(ans.pop())