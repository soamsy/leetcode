def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    def traverse(node):
        if not node:
            return (-1, -1)
        
        left_longest, left_diameter = traverse(node.left)
        right_longest, right_diameter = traverse(node.right)
        diameter = max(left_longest + right_longest + 2, left_diameter, right_diameter)
        return (max(left_longest, right_longest) + 1, diameter)
    
    _, diameter = traverse(root)
    return diameter