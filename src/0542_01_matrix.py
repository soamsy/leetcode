import collections
def updateMatrix(mat: list[list[int]]) -> list[list[int]]:
    m, n = len(mat), len(mat[0])
    q = collections.deque()
    
    for x, row in enumerate(mat):
        for y, val in enumerate(row):
            if val == 0:
                q.appendleft((x, y, 0))
    
    result = [[None] * n for _ in range(m)]
    while q:
        x, y, dist = q.pop()
        if x < 0 or x >= m or y < 0 or y >= n:
            continue
        
        if result[x][y] is not None and result[x][y] <= dist:
            continue
        
        result[x][y] = dist
        
        q.appendleft((x + 1, y, dist + 1))
        q.appendleft((x, y + 1, dist + 1))
        q.appendleft((x - 1, y, dist + 1))
        q.appendleft((x, y - 1, dist + 1))
    
    return result