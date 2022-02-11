def cloneGraph(start: 'Node') -> 'Node':
    clones = {}
    def clone(node):
        if not node:
            return node
        if node.val in clones:
            return clones[node.val]
        new = Node(node.val)
        clones[new.val] = new
        new.neighbors = [clone(n) for n in node.neighbors]
        return new
    
    return clone(start)