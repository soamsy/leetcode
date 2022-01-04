def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return None
    
    aligned_chars = map(lambda *x: x, *strs)
    length = 0
    for i, seq in enumerate(aligned_chars):
        if len(set(seq)) == 1:
            length = i + 1
        else:
            break
            
    return strs[0][:length]