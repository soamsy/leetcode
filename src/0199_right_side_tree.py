import collections
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    
    q = collections.deque()
    q.appendleft((root, 0))
    result = []
    while q:
        node, level = q.pop()
        if not node:
            continue
        if level >= len(result):
            result.append(node.val)
        
        q.appendleft((node.right, level + 1))
        q.appendleft((node.left, level + 1))
    
    return result