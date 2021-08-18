#Page 109 to page 241
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data        

#def createMin(a):
#    if not a:
#        return False
#    mid = len(a) // 2
#    n = Node(a[mid])
#    n.left = createMin(a[:mid])
#    n.right = createMin(a[(mid + 1):])
#    return n

def listOfDepths(root, depths, i):
    if not root:
        return
    if len(depths) == i:
        depths.append([root.data])
    else:
        depths[i].append(root.data)
    listOfDepths(root.left, depths, i + 1)
    listOfDepths(root.right, depths, i + 1)
    return depths

#a = [1, 2, 3, 4, 5, 6, 7]
#n = createMin(a) 
#print(listOfDepths(n, [], 0))