#Page 109 to page 241
#Subtree check (simple)
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def getpreOrder(root, seq):
    if not root:
        seq.append('X')
        return
    seq.append(root.data)
    getpreOrder(root.left, seq)
    getpreOrder(root.right, seq)
    
def checkSubtree(root1, root2):
    list1 = []
    getpreOrder(root1, list1)
    list2 = []
    str2 = getpreOrder(root2, list2)
    str1 = ' '.join(list(map(str, list1)))
    str2 = ' '.join(list(map(str, list2)))
    if str2 in str1:
        return True
    return False