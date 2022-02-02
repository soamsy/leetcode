import math

def arrangeCoins(n: int) -> int:
    
    # k(k+1)/2 == sum(1..k) == n
    # (k^2 + k)/2 == n
    # k^2 + k == 2n
    # k^2 + k + 1/4 == 2n + 1/4
    # (k + 1/2) == sqrt(2n + 1/4)
    # k == sqrt(2n + 1/4) - 1/2
    
    return int(math.floor(math.sqrt(2*n + .25) - .5))