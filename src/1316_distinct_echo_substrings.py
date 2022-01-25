def distinctEchoSubstrings(text: str) -> int:
    strings = set()
    for i in range(len(text) - 1):
        left = i
        right = i + 1
        while left >= 0 and right < len(text):
            if text[right] == text[i] and text[left] == text[i+1]:                    
                a = text[left:i+1] 
                b = text[i+1:right+1]
                if a == b:
                    strings.add(a)
            left -= 1
            right += 1
    
    return len(strings)