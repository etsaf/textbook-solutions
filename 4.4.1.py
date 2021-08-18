#Page 109 to page 241
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def findHeight(node):
    if not node:
        return -1
    return max(findHeight(node.left), findHeight(node.right)) + 1

def checkBalanced(node):
    if not node:
        return True
    if abs(findHeight(node.left) - findHeight(node.right)) > 1:
        return False
    if checkBalanced(node.left) and checkBalanced(node.right):
        return True
    return False