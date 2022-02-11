def setZeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = set()
    cols = set()
    m, n = len(matrix), len(matrix[0])
    
    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.add(x)
                cols.add(y)
                
    for x in rows:
        for y in range(n):
            matrix[x][y] = 0
    
    for y in cols:
        for x in range(m):
            matrix[x][y] = 0