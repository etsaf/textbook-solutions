#Page 109 to page 241
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data        

def createMin(a):
    if not a:
        return False
    mid = len(a) // 2
    n = Node(a[mid])
    n.left = createMin(a[:mid])
    n.right = createMin(a[(mid + 1):])
    return n

def printPreOrder(node): 
    if not node:
        return
    print(node.data)
    printPreOrder(node.left) 
    printPreOrder(node.right)

#a = [1, 2, 3, 4, 5, 6, 7] 
#n = createMin(a) 
#print (printPreOrder(n))


#mid = len(a) // 2 #find root
#depth = 0
#levels = []
#num = 1
#i = 0
#while num: #find depth
#    i += 1
#    num1 = num + 2 ** i
#    if num <= len(a) and num1 >= len(a):
#        depth = i
#        break
#    num = num1
#k = len(a)
#for j in range(depth): #find distribution across levels
#    if k >= 2 ** j:
#        levels.append(2 ** j)
#        k -= 2 ** j
#    else:
#        levels.append(k)