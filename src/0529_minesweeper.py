import collections
def updateBoard(board: list[list[str]], click: list[int]) -> list[list[str]]:
    a, b = click[0], click[1]
    m, n = len(board), len(board[0])
    if board[a][b] == 'M':
        board[a][b] = 'X'
        return board
    
    def square_count(x, y, char):
        count = 0
        for i in range(max(0, x-1),min(x+2, m)):
            for j in range(max(0, y-1), min(y+2, n)):
                if i == x and j == y:
                    continue
                count += 1 if board[i][j] == char else 0
        return count

    q = collections.deque()
    q.appendleft((a, b))
    while q:
        x, y = q.pop()
        
        if x < 0 or x >= m or y < 0 or y >= n:
            continue
        
        if board[x][y] != 'E':
            continue
        
        num_mines = square_count(x, y, 'M')
        if num_mines > 0:
            board[x][y] = str(num_mines)
            continue
        else:
            board[x][y] = 'B'
            
        q.appendleft((x-1, y-1))
        q.appendleft((x, y-1))
        q.appendleft((x+1, y-1))
        q.appendleft((x-1, y))
        q.appendleft((x+1, y))
        q.appendleft((x-1, y+1))
        q.appendleft((x, y+1))
        q.appendleft((x+1, y+1))

    return board