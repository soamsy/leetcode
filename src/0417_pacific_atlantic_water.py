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
    
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    def flood(q, island):
        while q:
            x, y = q.pop()
            island[x][y] = True
            for a, b in directions:
                if inBounds(x+a, y+b) and heights[x+a][y+b] >= heights[x][y]:
                    if not island[x+a][y+b]:
                        q.appendleft((x+a,y+b))
                
    flood(p, pacific)
    flood(a, atlantic)
    
    peaks = []
    for x in range(m):
        for y in range(n):
            if pacific[x][y] and atlantic[x][y]:
                peaks.append([x, y])
    
    return peaks