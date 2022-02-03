import collections
def findContentChildren(g: list[int], s: list[int]) -> int:
    s.sort(reverse=True)
    g.sort()
    count = 0
    for greed in g:
        while s and s[-1] < greed:
            s.pop()
        if not s:
            break
        s.pop()
        count += 1
    return count