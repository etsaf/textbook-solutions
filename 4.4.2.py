#Page 109 to page 241
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def findHeight(node):
    if not node:
        return -1
    leftHeight = findHeight(node.left)
    if leftHeight == float('inf'):
        return float('inf')
    rightHeight = findHeight(node.right)
    if leftHeight == float('inf'):
        return float('inf')
    difHeight = leftHeight - rightHeight
    if abs(difHeight) > 1:
        return float('inf')
    return max(findHeight(node.left), findHeight(node.right)) + 1

def checkBalanced(node):
    return findHeight(node) != float('inf')
