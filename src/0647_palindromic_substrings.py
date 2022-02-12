def countSubstrings(s: str) -> int:
    count = 0
    for i in range(len(s)):
        j = 0
        while 0 <= i-j and i+j < len(s) and s[i-j] == s[i+j]:
            count += 1
            j += 1
        
        j = 0
        while 0 <= i-j and i+j+1 < len(s) and s[i-j] == s[i+j+1]:
            count += 1
            j += 1
    
    return count