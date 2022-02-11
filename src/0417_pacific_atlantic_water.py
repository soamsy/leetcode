import collections
def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    m, n = len(heights), len(heights[0])
    pacific = [[False] * n for _ in range(m)]
    atlantic = [[False] * n for _ in range(m)]
    
    p = collections.deque()
    a = collections.deque()
    for i in range(m):
        p.appendleft((i,0))
        a.appendleft((i,n-1))
        
    for j in range(n):
        p.appendleft((0,j))
        a.appendleft((m-1,j))
        
    
    def inBounds(x, y):
        return 0 <= x < m and 0 <= y < n
    
    def flood(q, island):
        while q:
            x, y = q.pop()
            island[x][y] = True
            if inBounds(x+1, y) and heights[x+1][y] >= heights[x][y] and not island[x+1][y]:
                q.appendleft((x+1,y))
            if inBounds(x-1, y) and heights[x-1][y] >= heights[x][y] and not island[x-1][y]:
                q.appendleft((x-1,y))
            if inBounds(x, y+1) and heights[x][y+1] >= heights[x][y] and not island[x][y+1]:
                q.appendleft((x,y+1))
            if inBounds(x, y-1) and heights[x][y-1] >= heights[x][y] and not island[x][y-1]:
                q.appendleft((x,y-1))
                
    flood(p, pacific)
    flood(a, atlantic)
    
    peaks = []
    for x in range(m):
        for y in range(n):
            if pacific[x][y] and atlantic[x][y]:
                peaks.append([x, y])
    
    return peaks