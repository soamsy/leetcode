def climbStairs(n: int) -> int:
    stairs = [1, 1]
    for i in range(2, n + 1):
        stairs.append(stairs[-1] + stairs[-2])
    return stairs[n]