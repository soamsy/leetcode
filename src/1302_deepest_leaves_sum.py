from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    def fn(node, depth):
        if not node:
            return (0, depth)
        if not node.left and not node.right:
            return (node.val, depth)
        vl, dl = fn(node.left, depth + 1)
        vr, dr = fn(node.right, depth + 1)
        if dl < dr:
            return (vr, dr)
        elif dl > dr:
            return (vl, dl)
        else:
            return (vl + vr, dl)
        
    return fn(root, 0)[0]