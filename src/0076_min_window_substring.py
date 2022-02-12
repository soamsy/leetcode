import collections

def minWindow(s: str, t: str) -> str:
    chars = set(t)
    count = collections.Counter(t)
    numNotFound = len(chars)
    
    j = 0
    bestWindow = ""
    bestLength = float("infinity")
    
    for i in range(len(s)):
        if s[i] in chars:
            count[s[i]] -= 1
            if count[s[i]] == 0:
                numNotFound -= 1
        if numNotFound == 0:
            while numNotFound == 0:
                if s[j] in chars:
                    count[s[j]] += 1
                    if count[s[j]] == 1:
                        numNotFound += 1
                j += 1
            window = s[j-1:i+1]
            if len(window) < bestLength:
                bestLength = len(window)
                bestWindow = window
    
    return bestWindow