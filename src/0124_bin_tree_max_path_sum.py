from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: Optional[TreeNode]) -> int:
    def fn(node):
        if not node.left and not node.right:
            return (node.val, node.val)
        if not node.left or not node.right:
            subOpt, subDep = fn(node.left if node.left else node.right)
            depth = node.val + max(subDep, 0)
            return (max(depth, subDep, subOpt), depth)
        
        lOpt, lDep = fn(node.left)
        rOpt, rDep = fn(node.right)
        depth = node.val + max(lDep, rDep, 0)
        myOpt = node.val + lDep + rDep
        opt = max(depth, lDep, rDep, myOpt, lOpt, rOpt)
        return (opt, depth)
    
    return fn(root)[0]