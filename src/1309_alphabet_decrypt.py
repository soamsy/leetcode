def freqAlphabets(s: str) -> str:
    i = len(s) - 1
    final = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    while i >= 0:
        if s[i] == "#":
            final.append(int(s[i-2:i]))
            i -= 3
        else:
            final.append(int(s[i:i+1]))
            i -= 1
    
    return ''.join([alphabet[d-1] for d in reversed(final)])