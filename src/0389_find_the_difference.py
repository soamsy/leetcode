import collections
def findTheDifference(s: str, t: str) -> str:
    count = collections.Counter(s)
    for c in t:
        if c in count:
            count[c] -= 1
            if count[c] == 0:
                del count[c]
        else:
            return c
    return next(count.keys())