import math
def nthMagicalNumber(n: int, a: int, b: int) -> int:
    if a > b:
        a, b = b, a
        
    if a == b:
        return n * a % (10**9 + 7)
        
    lowest_mult = math.lcm(a, b)
    
    high = a * n
    low = a
    while low <= high:
        mid = (low + high) / 2
        options = [a * (mid // a), b * (mid // b)]
        backups = [a * (mid // a) + a, b * (mid // b) + b]
        mid = int(max(options))
        if mid < low:
            mid = int(min([x for x in backups if low <= x <= high]))
        
        num_a = mid // a
        num_b = mid // b
        num_overlap = mid // lowest_mult
        total = num_a + num_b - num_overlap
        
        if total > n:
            high = mid - 1
        elif total < n:
            low = mid + 1
        else:
            return mid % (10**9 + 7)
    
    return low % (10**9 + 7)