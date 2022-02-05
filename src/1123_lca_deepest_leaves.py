from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def fn(node, d=0):
        if not node:
            return (None, d-1)
        
        l_ancestor, l_depth = fn(node.left, d + 1)
        r_ancestor, r_depth = fn(node.right, d + 1)
        if l_depth == r_depth:
            return (node, l_depth)
        elif l_depth > r_depth:
            return l_ancestor, l_depth
        else:
            return r_ancestor, r_depth
        
    return fn(root)[0]