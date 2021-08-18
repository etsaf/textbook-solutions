#Page 109 to page 241
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.parent = None

def insert(root, data): #given: tree, new node
    if not root:
        return Node(data)
    if data <= root.data:
        place = insert(root.left, data)
        root.left = place
        place.parent = root
    else:
        place = insert(root.right, data)
        root.right = place
        place.parent = root
    return root

def mostLeftChild(node):
    if not node:
        return None
    while node.left:
        node = node.left
    return node

def successor(node):
    if not node:
        return None
    if node.right:
        return mostLeftChild(node.right)
    old = node
    new = old.parent
    while new and new.left != old:
        old = new
        new = new.parent
    return new