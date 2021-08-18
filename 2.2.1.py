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
            
    def returnKthtolast(self, k):
        current = self
        d = []
        runner = self
        bv = True
        for i in range(k):
            if runner == None:
                return None
            runner = runner.next
        while current != None:
            if runner == None:
                bv = False
            if bv:
                current = current.next
                runner = runner.next
            else:
                d.append(str(current.data))
                current = current.next
        return ' '.join(d)

node1 = Node(1)
node1.appendToTail(Node(2))
node1.appendToTail(Node(3))
node1.appendToTail(Node(4))
node1.appendToTail(Node(5))
node1.appendToTail(Node(6))
node1.appendToTail(Node(7))
print(node1.returnKthtolast(3))