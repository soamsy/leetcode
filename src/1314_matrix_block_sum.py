import copy

def matrixBlockSum(mat: list[list[int]], k: int) -> list[list[int]]:
    m, n = len(mat), len(mat[0])
    prefix = copy.deepcopy(mat)
    
    for i in range(1, m):
        prefix[i][0] += prefix[i-1][0]
        
    for j in range(1, n):
        prefix[0][j] += prefix[0][j-1]
    
    for i in range(1, m):
        for j in range(1, n):
            prefix[i][j] += prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
            
    result = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            
            up = max(0, i - k)
            down = min(m - 1, i + k)
            left = max(0, j - k)
            right = min(n - 1, j + k)
            
            result[i][j] = prefix[down][right]
            if up != 0:
                result[i][j] -= prefix[up-1][right]
            
            if left != 0:
                result[i][j] -= prefix[down][left - 1]
                
            if up != 0 and left != 0:
                result[i][j] += prefix[up-1][left-1]
            
    return result