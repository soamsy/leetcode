import math
import copy

def maxSideLength(mat: list[list[int]], threshold: int) -> int:
    if len(mat) == 0:
        return 0
    m, n = len(mat), len(mat[0])
    max_square = min(m, n)
    
    sum_mat = copy.deepcopy(mat)
    
    for i in range(1, m):
        sum_mat[i][0] += sum_mat[i-1][0]
        
    for j in range(1, n):
        sum_mat[0][j] += sum_mat[0][j-1]
    
    for i in range(1, m):
        for j in range(1, n):
            sum_mat[i][j] += sum_mat[i-1][j] + sum_mat[i][j-1] - sum_mat[i-1][j-1]
    
    def scan_for_fitting_square(length):
        for i in range(length - 1, m):
            for j in range(length - 1, n):
                a, b = i - length, j - length
                val = sum_mat[i][j]
                if a >= 0:
                    val -= sum_mat[a][j]
                if b >= 0:
                    val -= sum_mat[i][b]
                if a >= 0 and b >= 0:
                    val += sum_mat[a][b]
                
                if val <= threshold:
                    return True
        return False
                
                
    answer = 0
    low = 1
    high = max_square
                
    while low <= high:
        mid = (low + high) // 2
        if scan_for_fitting_square(mid):
            low = mid + 1
            answer = mid
        else:
            high = mid - 1
    return answer