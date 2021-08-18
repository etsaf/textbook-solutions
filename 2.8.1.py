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
    
def loop(self):
    slow = self
    fast = self
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if fast == None:
        return None
    slow = self
    while slow != fast:
        fast = fast.next
        slow = slow.next
    return fast

node1 = Node(3)
node1.appendToTail(Node(1))
node1.appendToTail(Node(5))
node1.appendToTail(Node(9))
node2 = Node(4)
node3 = Node(7)
node4 = Node(2)
node5 = Node(1)
node1.appendToTail(node2)
node2.appendToTail(node3)
node2.appendToTail(node4)
node2.appendToTail(node5)
node2.apppendToTail(node3)


print(loop(node1))