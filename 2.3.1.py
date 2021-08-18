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
            
    def deleteMiddle(n):
        next = n.next
        n.data = next.data
        n.next = next.next

node1 = Node(1)
node1.appendToTail(Node(2))
node1.appendToTail(Node(3))
node2 = Node(4)
node1.appendToTail(node2)
node1.appendToTail(Node(5))
node1.appendToTail(Node(6))
node1.appendToTail(Node(7))
node2.deleteMiddle()
node1.traverse()