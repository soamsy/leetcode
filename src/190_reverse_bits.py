def reverseBits(n: int) -> int:
    s = str(bin(n))
    s = s[2:]
    s = ((32 - len(s)) * "0") + s
    return int('0b' + (''.join(list(reversed(s)))), 2)