def findKthNumber(n: int, k: int) -> int:
    k -= 1
    curr = [1]
    max_level = len(str(n))

    def currNumber():
        return int(''.join([str(x) for x in curr]))

    while k > 0 and len(curr) <= max_level:
        stepsToInc = 0
        num_levels = max_level - len(curr)
        for level in range(num_levels):
            stepsToInc += 10 ** level

        low = currNumber() * 10 ** num_levels
        high = (currNumber() + 1) * 10 ** num_levels - 1
        high = min(high, n)
        available_at_level = max(0, high - low + 1)
        stepsToInc += available_at_level

        if k - stepsToInc >= 0 and curr[-1] != 9:
            k -= stepsToInc
            curr[-1] += 1
        else:
            k -= 1
            curr.append(0)   

    return currNumber()


# for i in range(1, 124):
    # print(findKthNumber(123, i))