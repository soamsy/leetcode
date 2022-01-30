def numIslands(grid: list[list[str]]) -> int:
    m = len(grid)
    n = len(grid[0])
    def idx(x, y):
        return n * x + y
    
    uf = {}
    
    total_islands = 0
    for x in range(m):
        for y in range(n):
            i = idx(x, y)
            uf[i] = i
            if grid[x][y] == '1':
                total_islands += 1
                
    def find(i):
        is_root = uf[i] == i
        if not is_root:
            uf[i] = find(uf[i])
        return uf[i]
    
    def union(a, b):
        nonlocal total_islands
        rootA = find(a)
        rootB = find(b)
        if rootA != rootB:
            uf[rootA] = rootB
            total_islands -= 1
    
    for x in range(m):
        for y1, y2 in zip(range(n), range(1, n)):
            if grid[x][y1] == "1" and grid[x][y2] == "1":
                union(idx(x, y1), idx(x, y2))
    
    for y in range(n):
        for x1, x2 in zip(range(m), range(1, m)):
            if grid[x1][y] == "1" and grid[x2][y] == "1":
                union(idx(x1, y), idx(x2, y))
    
    return total_islands