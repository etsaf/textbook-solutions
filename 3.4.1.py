from collections import deque
#stack = deque()
#stack.append('a')
#stack.append('b')
#print(stack.pop())
#print(stack.pop())
#class Stack:

    #def __init__(self):
        #self.stack = []

    #def pop(self):
        #if len(self.stack) < 1:
            #return None
        #return self.stack.pop()

    #def push(self, item):
        #self.stack.append(item)

    #def size(self):
        #return len(self.stack)
class MyQueue:
    
    def __init__(self):
        self.stackOld = list()
        self.stackNew = list()

    def size(self):
        return len(self.stackOld) + len(self.stackNew)

    def remove(self):
        if len(self.stackOld) == 0:
            shift(self)
        self.stackOld.pop()

    def add(self):
        self.stackNew.append(self)

    def shift(self):
        if len(self.stackOld) == 0:
            while len(self.stackNew) > 0:
                self.stackOld.append(self.stackNew.pop())

    def peek(self):
        if len(self.stackOld) == 0:
            shift(self)
        a = self.stackOld.pop()  
        self.stackOld.append(a)
        return a

stack = Stack()
stack.push(8)
stack.push(6)
stack.push(3)
stack.push(7)
print(stack.minimum())