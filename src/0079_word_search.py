def exist(board: list[list[str]], word: str) -> bool:
    m, n = len(board), len(board[0])
    consumed = set()
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    def backtrack(i, j, c):
        if c >= len(word):
            return True
        
        if not (0 <= i < m and 0 <= j < n):
            return False
        
        if (i, j) in consumed:
            return False
        
        if word[c] != board[i][j]:
            return False
        
        consumed.add((i, j))
        for d in dirs:
            if backtrack(i+d[0], j+d[1], c+1):
                consumed.remove((i, j))
                return True
        consumed.remove((i, j))
        return False
    
    for i in range(m):
        for j in range(n):
            if backtrack(i, j, 0):
                return True
    return False