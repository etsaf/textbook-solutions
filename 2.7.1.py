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
    
def intersection(self, other):
    node1 = self
    node2 = other
    tail1 = None
    tail2 = None
    len1 = 0
    len2 = 0
    while node1.next != None:
        len1 += 1
        node1 = node1.next
    len1 += 1
    tail1 = node1.next
    while node2.next != None:
        len2 += 1
        node2 = node2.next
    len2 += 1
    tail2 = node2.next
    if tail1 != tail2:
        return False
    point1 = self
    point2 = other
    if len1 > len2:
        for i in range(len1 - len2):
            point1 = point1.next
    elif len2 > len1:
        for i in range(len2 - len1):
            point2 = point2.next
    while point1 != None:
        if point1 == point2:
            return point1.data
        point1 = point1.next
        point2 = point2.next

node1 = Node(3)
node1.appendToTail(Node(1))
node1.appendToTail(Node(5))
node1.appendToTail(Node(9))
node2 = Node(4)
node2.appendToTail(Node(6))
node3 = Node(7)
node4 = Node(2)
node5 = Node(1)
node3.appendToTail(node4)
node3.appendToTail(node5)
node1.appendToTail(node3)
node2.appendToTail(node3)
print(intersection(node1, node2))