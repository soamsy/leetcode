def isPossibleDivide(nums: list[int], k: int) -> bool:
    if len(nums) % k != 0:
        return False
    
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
    
    uniques = sorted(list(set(nums)))
    
    while counts:
        chunk = []
        i = len(uniques) - 1
        while len(chunk) < k and i >= 0:
            next = uniques[i]
            if not chunk or next == chunk[-1] - 1:
                chunk.append(next)
                counts[next] -= 1
                if counts[next] <= 0:
                    del counts[next]
                    uniques.pop(i)
                i -= 1
            elif next == chunk[-1]:
                i -= 1
            else:
                return False
        if len(chunk) != k:
            return False
    return True