def countBits(n: int) -> list[int]:
    result = [0]
    for i in range(1,n+1):
        count = 0
        test = ~(i - 1)
        while test & 1 == 0:
            test >>= 1
            count += 1
        result.append(result[i-1] - count + 1)
    return result