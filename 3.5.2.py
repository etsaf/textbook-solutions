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
    a1 = stack1.pop()
    a2 = stack1.pop()
    stack2.push(min(a1, a2))
    stack2.push(max(a1, a2))
    while stack1.size() > 0:
        a = stack1.pop()
        prev = stack2.pop()
        notIn = True
        transfer = 0
        while notIn:
            nex = stack2.pop()
            if prev >= a and nex <= a:
                stack2.push(nex)
                stack2.push(a)
                stack2.push(prev)
                for i in range(transfer):
                    stack2.push(stack1.pop())
                notIn = False
            elif stack2.size() == 0:
                stack2.push(a)
                stack2.push(nex)
                stack2.push(prev)
                for i in range(transfer):
                    stack2.push(stack1.pop())
                notIn = False
            else:
                stack1.push(prev)
                transfer += 1
                prev = nex
    return stack2

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