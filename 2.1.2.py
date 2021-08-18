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
        current = self
        runner = self
        while current.next != None:
            runner = current
            while runner.next != None:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

node1 = Node(1)
node1.appendToTail(Node(2))
node1.appendToTail(Node(3))
node1.appendToTail(Node(2))
node1.appendToTail(Node(2))
node1.appendToTail(Node(4))
node1.appendToTail(Node(1))
node1.removeDups()
node1.traverse()