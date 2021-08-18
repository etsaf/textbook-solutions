#from collections import deque
#stack = deque()
#stack.append('a')
#stack.append('b')
#print(stack.pop())
#print(stack.pop())
class SetOfStacks:

    def __init__(self):
        self.stack = [[]]

    def pop(self):
        if len(self.stack[0]) < 1:
            return None
        elif len(self.stack[len(self.stack) - 1]) >= 1:
            return self.stack[len(self.stack) - 1].pop()
        elif len(self.stack[len(self.stack) - 1]) == 0:
            

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)
    
stack = Stack()
stack.push(8)
stack.push(6)
stack.push(3)
stack.push(7)
print(stack.minimum())