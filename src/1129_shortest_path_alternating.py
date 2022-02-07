import collections
def shortestAlternatingPaths(n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
    red = {}
    for a, b in redEdges:
        red[a] = red.get(a, []) + [b]
    blue = {}
    for a, b in blueEdges:
        blue[a] = blue.get(a, []) + [b]
    
    result = []
    for x in range(n):
        q = collections.deque()
        blueVisited = set()
        redVisited = set()
        q.appendleft((0, 0, False))
        q.appendleft((0, 0, True))
        shortest = -1
        while q and shortest == -1:
            node, dist, isBlue = q.pop()
            visited = blueVisited if isBlue else redVisited
            if node in visited:
                continue
            
            visited.add(node)
                
            if node == x:
                shortest = dist
                continue
            
            edges = blue if isBlue else red
            for target in edges.get(node, []):
                q.appendleft((target, dist + 1, not isBlue))
        result.append(shortest)
    return result