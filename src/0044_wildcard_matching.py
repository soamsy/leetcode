def isMatch(s: str, p: str) -> bool:
    cache = {}
    def recur(a, b):
        if a >= len(s) and b >= len(p):
            return True
        if b >= len(p):
            return False
        if a >= len(s) and p[b] != '*':
            return False
        
        if (a, b) in cache:
            return cache[(a, b)]
        
        if p[b] == '*':
            if a >= len(s):
                cache[(a, b)] = recur(a, b + 1)
            else:
                cache[(a, b)] = recur(a + 1, b) or recur(a, b + 1)
        else:
            if s[a] == p[b] or p[b] == '?':
                cache[(a, b)] = recur(a+1, b+1)
            else:
                cache[(a, b)] = False
                
        return cache[(a, b)]
    return recur(0, 0)