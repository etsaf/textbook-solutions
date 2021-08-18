from collections import deque
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
        self.stack.append(item)

    def size(self):
        return len(self.stack)

    def peek(self):
        if len(self.stack) < 1:
            return None
        a = self.stack.pop()
        self.stack.append(a)
        return a

def sortStack(self):
    stack1 = self
    stack2 = Stack()
    stackFin = Stack()
    while stack1.size() > 0 or stack2.size() > 0:
        a = stack1.pop()
        while stack1.size() > 0:
            b = stack1.pop()
            if b > a:
                stack2.push(a)
                a = b
            else:
                stack2.push(b)
        stackFin.push(a)
        while stack2.size() != 0:
            stack1.push(stack2.pop())
    return stackFin

stack = Stack()
stack.push(8)
stack.push(6)
stack.push(3)
stack.push(7)
ans = sortStack(stack)
while ans.size() != 0:
    print(ans.pop())