def sumZero(n: int) -> list[int]:
    half = n // 2
    pos = list(range(1, half + 1))
    neg = [-x for x in pos]
    if n % 2 != 0:
        return pos + neg + [0]
    else:
        return pos + neg