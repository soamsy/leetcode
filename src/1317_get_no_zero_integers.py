def getNoZeroIntegers(n: int) -> list[int]:
    for i in range(1,n):
        if "0" not in str(i) and "0" not in str(n - i):
            return [i, n-i]
    return [0, 0]