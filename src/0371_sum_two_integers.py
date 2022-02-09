def getSum(a: int, b: int) -> int:
    mask = 0xffffffff
    a &= mask
    while b != 0:
        add = (a^b) & mask
        carry = ((a&b)<<1) & mask
        a = add
        b = carry

    isNegative = (a>>31) & 1
    if isNegative:
        return ~(a^mask)
    
    return a