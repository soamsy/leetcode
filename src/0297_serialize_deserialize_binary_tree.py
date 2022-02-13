import collections
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        level = [root]
        result = []
        while level:
            result.extend([str(n.val) if n else 'null' for n in level])
            level = [c for n in [n for n in level if n] for c in [n.left, n.right]]
            
        return ','.join(result)
            
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        strs = data.split(',')[::-1]
        if not strs:
            return None
        
        def getNext():
            val = strs.pop()
            if val == 'null':
                return None
            return TreeNode(int(val))
        
        root = getNext()
        q = collections.deque()
        q.append(root)
        while q and strs:
            parent = q.popleft()
            parent.left = getNext()
            parent.right = getNext()
            if parent.left:
                q.append(parent.left)
            if parent.right:
                q.append(parent.right)
            
        return root