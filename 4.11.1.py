#Page 109 to page 241
#Random node
from random import randrange

class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.size = 1
        
def insert(root, data):
    if not root:
        return Node(data)
    if data <= root.data:
        if not root.left:
            root.left = Node(data)
        else:
            insert(root.left, data)
    else:
        if not root.right:
            root.right = Node(data)
        else:
            insert(root.right, data)
    root.size += 1

def find(root, data):
    if not root:
        return None
    if root.data == data:
        return root
    if data <= root.data:
        return find(root.left, data)
    return find(root.right, data)

def getRandom(root):
    leftsize = 0
    rightsize = 0
    if root.left:
        leftsize = root.left.size
    if root.right:
        rightsize = root.right.size
    x = randrange(leftsize + rightsize + 2)
    if x == leftsize:
        return root
    elif x < leftsize:
        getRandom(root.left)
    else:
        getRandom(root.right)