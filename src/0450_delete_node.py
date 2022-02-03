from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    def delete(parent, is_left, node, key):
        if not node:
            return None
        
        if key == node.val and not node.left and not node.right and not parent:
            return None
        
        new_root = None
        def hookToParent(n):
            nonlocal new_root
            if not parent:
                new_root = n
            elif is_left:
                parent.left = n
            else:
                parent.right = n

        if key == node.val:
            if not node.left and not node.right:
                hookToParent(None)
            elif node.left and node.right:
                searchParent = node
                search = node.right
                while search.left:
                    searchParent = search
                    search = search.left
                if node.right == search:
                    search.left = node.left
                    hookToParent(search)
                else:
                    searchParent.left = search.right
                    search.left = node.left
                    search.right = node.right
                    hookToParent(search)
                
            elif node.left:
                hookToParent(node.left)
            else:
                hookToParent(node.right)
        elif key < node.val:
            delete(node, True, node.left, key)
        else:
            delete(node, False, node.right, key)
            
        return node if new_root is None else new_root
    return delete(None, True, root, key)