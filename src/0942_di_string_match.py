def diStringMatch(s: str) -> list[int]:
    n = len(s)
    dlen = len([c for c in s if c == 'D'])
    decreasing = iter(range(dlen - 1, -1, -1))
    seq = [dlen]
    increasing = iter(range(dlen + 1, n + 1))
    
    i = 0
    while i < n:
        if s[i] == 'I':
            seq.append(next(increasing))
        else:
            seq.append(next(decreasing))
        i += 1
        
    return seq