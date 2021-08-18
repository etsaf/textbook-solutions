#Page 109 to page 241
#Lowest common ancestor with links to parents
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.parent = None

def depth(node):
    depth = 0
    while node:
        node = node.parent
        depth += 1
    return depth

def up(node, diff):
    while diff > 0 and node:
        node = node.parent
        diff -= 1
    return node

def commonAnc(p, q):
    diff = depth(p) - depth(q)
    if diff > 0:
        higher, lower = q, p
    else:
        higher, lower = p, q
    lower = up(lower, abs(diff))
    while lower != higher and lower and higher:
        lower = lower.parent
        higher = higher.parent
    return higher