class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumEvenGrandparent(root: TreeNode) -> int:
    def fn(node):
        if not node:
            return 0
        
        if node.val % 2 != 0:
            return fn(node.left) + fn(node.right)
        
        gc = []
        if node.left and node.left.left:
            gc.append(node.left.left)
        if node.left and node.left.right:
            gc.append(node.left.right)
        if node.right and node.right.left:
            gc.append(node.right.left)
        if node.right and node.right.right:
            gc.append(node.right.right)
        
        if not gc:
            return 0
        else:
            return sum([n.val for n in gc]) + fn(node.left) + fn(node.right)
    
    return fn(root)