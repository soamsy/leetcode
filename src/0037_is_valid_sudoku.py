def isValidSudoku(board: list[list[str]]) -> bool:
    rows = board
    cols = list(map(lambda *r: r, *board))
    squares = [[] for i in range(9)]
    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            index = (i // 3) * 3 + (j // 3)
            squares[index].append(board[i][j])
            
    def validBlock(block):
        filledCells = [x for x in block if x != '.']
        return len(filledCells) == len(set(filledCells))
    
    def allUniques(blocks):
        return all(map(validBlock, blocks))
    
    return allUniques(rows) and allUniques(cols) and allUniques(squares)