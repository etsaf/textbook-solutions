#Page 109 to page 241
#BST sequence - all arrays that could have led to a given tree
class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def weave(first, second, prefix, result):
    if first:
        lf = len(first)
    else:
        lf = 0
    if second:       
        ls = len(second)
    else:
        ls = 0  

    if lf == 0 or ls == 0:
        ans = []
        ans.extend(prefix)
        if first:
            ans.extend(first)
        if second:   
            ans.extend(second)
        result.append(ans)
        return

    if lf:
        pre = first.pop(0)
        prefix.append(pre)
        weave(first, second, prefix, result)
        prefix.pop()
        first.insert(0, pre)
 
    if ls:
        pre = second.pop(0)
        prefix.append(pre)
        weave(first, second, prefix, result)
        prefix.pop()
        second.insert(0, pre)   


def allseq(root):
    if not root:
        return []
    ans = []
    prefix = [root.data]
    if root.left:
        leftseq = allseq(root.left)
    else:
        leftseq = [[]]
    if root.right:
        rightseq = allseq(root.right)
    else:
        rightseq = [[]]
    for left in leftseq:
        for right in rightseq:
            weaved = []
            weave(left, right, prefix, weaved)
            for i in weaved:
                ans.append(i)
    return ans