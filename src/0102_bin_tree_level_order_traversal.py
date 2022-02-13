import collections
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> list[list[int]]:
    
    q = collections.deque()
    q.append((root, 0))
    
    result = []
    levelNodes = []
    lastLevel = 0
    while q:
        node, level = q.popleft()
        if not node:
            continue
        
        if level == lastLevel:
            levelNodes.append(node.val)
        else:
            lastLevel = level
            result.append(levelNodes)
            levelNodes = [node.val]
        
        q.append((node.left, level + 1))
        q.append((node.right, level + 1))
        
    if levelNodes:
        result.append(levelNodes)
    return result