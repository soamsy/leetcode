def rangeBitwiseAnd(left: int, right: int) -> int:
    count = right - left + 1
    bit = 0
    
    for i in [2**n for n in range(31, -1, -1)]:
        bit <<= 1
        if count <= i <= left % (i*2) <= right % (i*2):
            bit |= 1

    return bit