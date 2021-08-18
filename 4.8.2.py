#Page 109 to page 241
#Lowest common ancestor without links to parents
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def commonAnc(root, p, q):
    if not root:
        return None
    if root == p or root == q:
        return root
    commAnc_l = commonAnc(root.left, p, q)
    commAnc_r = commonAnc(root.right, p, q)
    if commAnc_l and commAnc_r:
        return root
    if commAnc_l:
        return commAnc_l
    return commAnc_r