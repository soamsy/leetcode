def xorQueries(arr: list[int], queries: list[list[int]]) -> list[int]:
    prefix = arr[:]
    for i in range(1, len(prefix)):
        prefix[i] ^= prefix[i-1]
        
    results = []
    for l, r in queries:
        if l <= 0:
            results.append(prefix[r])
        else:
            results.append(prefix[r] ^ prefix[l-1])
    return results