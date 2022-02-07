def numEquivDominoPairs(dominoes: list[list[int]]) -> int:
    count = collections.Counter([tuple(sorted(d)) for d in dominoes])
    return sum([math.comb(v, 2) if v > 1 else 0 for v in count.values()])