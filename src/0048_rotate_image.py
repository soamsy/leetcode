from math import ceil

def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    
    def next(x, y):
        return y, m-x-1
        
    halfwayIncludeMid = int(ceil(m / 2))
    halfway = m // 2
    for a1 in range(halfwayIncludeMid):
        for a2 in range(halfway):
            b1, b2 = next(a1, a2)
            c1, c2 = next(b1, b2)
            d1, d2 = next(c1, c2)
            matrix[a1][a2], matrix[b1][b2], matrix[c1][c2], matrix[d1][d2] = \
            matrix[d1][d2], matrix[a1][a2], matrix[b1][b2], matrix[c1][c2]
    
    return matrix