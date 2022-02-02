import collections

def findAnagrams(syy: str, p: str) -> list[int]:
    count = collections.Counter(p)
    
    def addChars(c, amount):
        count[c] = count.get(c, 0) + amount
        if count[c] == 0:
            del count[c]

    i = 0
    j = 0
    result = []
    while i <= j < len(syy):
        addChars(syy[j], -1)
        j += 1
        if j - i > len(p):
            addChars(syy[i], 1)
            i += 1
        if not count and j - i == len(p):
            result.append(i)

    return result