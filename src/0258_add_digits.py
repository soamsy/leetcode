def addDigits(num: int) -> int:
    while num // 10 > 0:
        num = sum([int(d) for d in str(num)])
    return num