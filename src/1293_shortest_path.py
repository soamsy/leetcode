def shortestPath(grid: list[list[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    q = collections.deque()
    
    visited = [[-1] * n for _ in range(m)]
    q.append((0, 0, k, 0))
    
    min_steps = float("infinity")
    max_possible_steps = m * n - 1
    
    while q:
        i, j, kleft, steps = q.popleft()
        
        if i < 0 or i >= m or j < 0 or j >= n:
            continue
            
        if grid[i][j]:
            kleft -= 1
            
        if kleft < 0:
            continue
            
        if i == m-1 and j == n-1:
            min_steps = min(steps, min_steps)

        if kleft <= visited[i][j]:
            continue
            
        visited[i][j] = kleft
        
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            q.append((i + x, j + y, kleft, steps + 1))
            
    return min_steps if min_steps <= max_possible_steps else -1