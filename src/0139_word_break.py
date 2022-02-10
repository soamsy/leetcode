from functools import cache
def wordBreak(s: str, wordDict: list[str]) -> bool:
    lookup = set(wordDict)
    
    @cache
    def fn(i):
        if i >= len(s):
            return True
        
        for j in range(i, len(s)):
            substr = s[i:j+1]
            if substr in lookup and fn(j+1):
                return True
        return False
    
    return fn(0)