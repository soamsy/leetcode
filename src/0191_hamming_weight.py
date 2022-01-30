def hammingWeight(n: int) -> int:
    return len([x for x in str(bin(n)) if x == '1'])