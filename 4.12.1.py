#Page 109 to page 241
#Paths with sum (any node to any node but downwards), brute force
from random import randrange

class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def countPathsNode(root, Sum, curr):
    if not root:
        return 0
    curr += root.data
    numPaths = 0
    if curr == Sum:
        numPaths += 1
    numPaths += countPathsNode(root.left, Sum, curr)
    numPaths += countPathsNode(root.right, Sum, curr)
    return numPaths

def countPaths(root, Sum):
    if not root:
        return 0
    rootpaths = countPathsNode(root, Sum, 0)
    leftpaths = countPaths(root.left, Sum)
    rightpaths = countPaths(root.right, Sum)
    return rootpaths + leftpaths + rightpaths