#Page 109 to page 241
#Subtree check not so simple
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def matchTree(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return root1.data == root2.data and matchTree(root1.left, root2.left) and matchTree(root1.right, root2.right)
    
def checkSubtree(root1, root2):
    if not root1:
        return False
    if not root2:
        return True
    if matchTree(root1, root2):
        return True
    return checkSubtree(root1.left, root2) or checkSubtree(root1.left, root2)