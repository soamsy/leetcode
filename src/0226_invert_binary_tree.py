from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def fn(node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        fn(node.left)
        fn(node.right)
        
    fn(root)
    return root