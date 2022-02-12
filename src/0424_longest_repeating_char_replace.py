import collections
def characterReplacement(self, s: str, k: int) -> int:
    counts = collections.Counter()
    j = 0
    maxCount = 0

    for i in range(len(s)):
        counts[s[i]] += 1
        maxCount = max(maxCount, counts[s[i]])
        spanLength = i - j + 1
        numDeletes = spanLength - maxCount
        if numDeletes > k:
            counts[s[j]] -= 1
            j += 1
            
    return len(s) - j