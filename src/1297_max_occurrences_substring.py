def maxFreq(s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    counts = {}
    for i in range(len(s) - minSize + 1):
        substr = s[i:i+minSize]
        if len(set(substr)) > maxLetters:
            continue
        counts[substr] = counts.get(substr, 0) + 1
    max_count = max(counts.values(), default=0)
    return max_count