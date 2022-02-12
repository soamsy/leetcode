from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def fn(a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        
        return a.val == b.val and fn(a.left, b.left) and fn(a.right, b.right)
    return fn(p, q)