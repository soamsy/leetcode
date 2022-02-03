def repeatedSubstringPattern(s: str) -> bool:
    low = 1
    high = len(s) // 2
    
    for divisor in range(high, low - 1, -1):
        if len(s) % divisor != 0:
            continue
            
        if all([a == b for a, b in zip(s, s[divisor:])]):
            return True
    return False