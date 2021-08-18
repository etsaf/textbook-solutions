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
            
    def removeDups(self):
        d = []
        node = self
        prev = None
        while node != None:
            if node.data in d:
                prev.next = node.next
            else:
                d.append(node.data)
                prev = node
            node = node.next

node1 = Node(1)
node1.appendToTail(Node(2))
node1.appendToTail(Node(3))
node1.appendToTail(Node(2))
node1.appendToTail(Node(2))
node1.appendToTail(Node(4))
node1.appendToTail(Node(1))
node1.removeDups()
node1.traverse()