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
    
    def length(self):
        node = self
        l = 1
        while node != None:
            l += 1
            node = node.next
        return l

def palindrome(self):
    rev = reverse(self)
    return isEqual(self, rev)

def reverse(self):
    head = self
    while self != None:
        n = Node(self.data)
        n.next = head
        head = n
        self = self.next
    return head

def isEqual(self, other):
    while self != None and other != None:
        if self.data != other.data:
            return False
        self = self.next
        other = other.next
    return True
node1 = Node(6)
node1.appendToTail(Node(2))
node1.appendToTail(Node(7))
node1.appendToTail(Node(7))
node1.appendToTail(Node(1))
node1.appendToTail(Node(6))

print(palindrome(node1))