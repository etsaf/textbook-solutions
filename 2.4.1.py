class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def appendToTail(self, new_node):
        node = self
        while node.next != None:
            node = node.next
        node.next = new_node
        
    def traverse(self):
        node = self
        while node != None:
            print(node.data)
            node = node.next
            
    def partition(self, x):
        lastsmall = None
        firstbig = None
        prev = self
        changehead = False
        newhead = ''
        if self.data >= x:
            firstbig = self
            changehead = True
        else:
            lastsmall = self
        node = self.next
        while node != None:
            if node.data >= x:
                if lastsmall != None and firstbig != None:
                    prev.next = node.next
                    lastsmall.next = node
                    node.next = firstbig
                    firstbig = node
                    node = prev.next
                elif lastsmall == None:
                    prev.next = node.next
                    node.next = firstbig
                    prev = prev.next
                    node = prev.next.next                    
                elif firstbig == None:
                    firstbig = node
                    prev = prev.next
                    node = prev.next.next                    
            else:
                if lastsmall == None:
                    lastsmall = node
                    newhead = node
                    prev = prev.next
                    node = prev.next.next
                elif firstbig == None:
                    lastsmall = node
                    prev = prev.next
                    node = prev.next.next                    
                else:
                    prev.next = node.next
                    lastsmall.next = node
                    node.next = firstbig
                    lastsmall = node
                    node = prev.next
            if changehead:
                return newhead.data
node1 = Node(3)
node1.appendToTail(Node(5))
node1.appendToTail(Node(8))
node1.appendToTail(Node(5))
node1.appendToTail(Node(10))
node1.appendToTail(Node(2))
node1.appendToTail(Node(1))
node1.partition(5)
node1.traverse()