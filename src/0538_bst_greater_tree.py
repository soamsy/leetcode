from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertBST(root: Optional[TreeNode]) -> Optional[TreeNode]:
    total = 0
    def traverse(node):
        nonlocal total
        if not node:
            return
        traverse(node.right)
        node.val += total
        total = node.val
        traverse(node.left)
    
    traverse(root)
    return root