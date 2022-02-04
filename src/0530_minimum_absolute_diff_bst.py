from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root: Optional[TreeNode]) -> int:
    xs = []
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        xs.append(node.val)
        traverse(node.right)
    
    traverse(root)
    min_diff = float("infinity")
    for a, b in zip(xs, xs[1:]):
        min_diff = min(min_diff, abs(a - b))
    
    return min_diff