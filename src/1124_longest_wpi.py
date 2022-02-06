import itertools
def longestWPI(hours: list[int]) -> int:
    prefix = list(itertools.accumulate([1 if h > 8 else -1 for h in hours]))[::-1]
    indexes = { c: i for i, c in enumerate(prefix) }
    
    highest = 0
    for i, v in enumerate(prefix):
        if v > 0:
            highest = max(highest, len(prefix) - i)
        elif v - 1 in indexes and i < indexes[v - 1]:
            highest = max(highest, indexes[v - 1] - i)
    
    return highest