def compress(chars: list[str]) -> int:
    i = 0
    counts = []
    while i < len(chars):
        char = chars[i]
        j = i
        while j < len(chars) and chars[j] == char:
            j += 1
        
        counts.append((char, j - i))
        i = j
    
    compressed = ''.join([c + str(count) if count != 1 else c for c, count in counts])
    for i, c in enumerate(compressed):
        chars[i] = c
        
    for i in range(len(compressed), len(chars)):
        chars.pop()