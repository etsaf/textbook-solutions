#Page 109 to page 241
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def checkBST(node, minn, maxx):
    if not node:
        return True
    if minn and node.data <= minn.data:
        return False
    if maxx and node.data >= maxx.data:
        return False
    return checkBST(node.left, minn, node) and checkBST(node.right, node, maxx)