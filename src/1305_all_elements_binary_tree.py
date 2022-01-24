class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getAllElements(root1: TreeNode, root2: TreeNode) -> list[int]:
    def toList(n):
        vals = []
        def fn(node):
            if not node:
                return
            if node.left:
                fn(node.left)
            vals.append(node.val)
            if node.right:
                fn(node.right)
        fn(n)
        return vals
    
    a = toList(root1)
    b = toList(root2)
    
    merged = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
            
    while i < len(a):
        merged.append(a[i])
        i += 1
    
    while j < len(b):
        merged.append(b[j])
        j += 1
        
    return merged