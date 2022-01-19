def solveSudoku(board: list[list[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    rows = board
    cols = list(map(lambda *r: r, *board))
    squares = [[] for i in range(9)]
    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            index = (i // 3) * 3 + (j // 3)
            squares[index].append(board[i][j])
            
    rowsets = [set(filter(lambda c: c != '.', block)) for block in rows]
    colsets = [set(filter(lambda c: c != '.', block)) for block in cols]
    squaresets = [set(filter(lambda c: c != '.', block)) for block in squares]
    
    total_cells = len(board) * 9
    
    def backtrack(i):
        if i >= total_cells:
            return True
        x = i // 9
        y = i % 9
        if board[x][y] != '.':
            return backtrack(i+1)
        
        rowset = rowsets[x]
        colset = colsets[y]
        squareset = squaresets[(x // 3) * 3 + (y // 3)]
        possible_nums = ((set([str(x) for x in range(1,10)]) - rowset) - colset) - squareset
        if not possible_nums:
            return False
        
        for num in possible_nums:
            board[x][y] = num
            rowset.add(num)
            colset.add(num)
            squareset.add(num)
            if backtrack(i+1):
                return True
            else:
                rowset.remove(num)
                colset.remove(num)
                squareset.remove(num)
                board[x][y] = '.'
        return False
            
    backtrack(0)