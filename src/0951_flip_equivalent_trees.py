from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flipEquiv(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def fn(left, right):
        if not left and not right:
            return True
        
        if (not left and right) or (left and not right):
            return False
        
        if left.val != right.val:
            return False
        
        return (fn(left.left, right.left) and fn(left.right, right.right)) or \
                (fn(left.left, right.right) and fn(left.right, right.left))
    
    return fn(root1, root2)