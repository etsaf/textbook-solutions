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
            
def sumlists(self, other):
    ans = 0
    placeInAns = 0
    tenth = 0
    node1 = self
    node2 = other
    while node1 != None or node2 != None:
        if node1 != None and node2 != None:
            x = node1.data + node2.data + tenth
            ans += (x % 10) * (10 ** placeInAns)
            tenth = x // 10
            placeInAns += 1
            node1 = node1.next
            node2 = node2.next
        elif node1 == None:
            x = node2.data + tenth
            ans += (x % 10) * (10 ** placeInAns)
            tenth = x // 10
            placeInAns += 1
            node2 = node2.next
        elif node2 == None:
            x = node1.data + tenth
            ans += (x % 10) * (10 ** placeInAns)
            tenth = x // 10
            placeInAns += 1
            node2 = node2.next
    ans += tenth * (10 ** placeInAns)
    return ans


node1 = Node(3)
node1.appendToTail(Node(2))
node1.appendToTail(Node(1))
node2 = Node(7)
node2.appendToTail(Node(8))
node2.appendToTail(Node(9))

a = sumlists(node1, node2)
print(a)