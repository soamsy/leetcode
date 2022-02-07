import collections
import math

def numEquivDominoPairs(dominoes: list[list[int]]) -> int:
    count = collections.Counter([tuple(sorted(d)) for d in dominoes])
    return sum([math.comb(v, 2) for v in count.values()])