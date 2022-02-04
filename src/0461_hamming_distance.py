import math
def hammingDistance(x: int, y: int) -> int:
    diff = x ^ y
    count = 0
    for i in range(32):
        count += diff & 1
        diff >>= 1
    
    return count