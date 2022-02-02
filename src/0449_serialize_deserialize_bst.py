import json
from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize(root: Optional[TreeNode]) -> str:
    """Encodes a tree to a single string.
    """
    def fn(node):
        if not node:
            return None
        
        parent = {}
        children = []
        children.append(fn(node.left))
        children.append(fn(node.right))
        
        if any(children):
            parent[node.val] = children
        else:
            parent[node.val] = None
        return parent
    return json.dumps(fn(root))
    
    

def deserialize(data: str) -> Optional[TreeNode]:
    """Decodes your encoded data to tree.
    """
    
    def fn(m):
        if not m:
            return None
        
        k = list(m.keys())[0]
        parent = TreeNode(k)
        children = m[k]
        if children:
            parent.left = fn(children[0])
            parent.right = fn(children[1])
        return parent
    
    return fn(json.loads(data))