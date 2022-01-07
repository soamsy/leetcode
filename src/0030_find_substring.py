def findSubstring(s: str, words: list[str]) -> list[int]:
    indexes = set()
    word_length = len(words[0])
    total_chars = word_length * len(words)
    
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
    for i in range(len(s) - total_chars + 1):
        curr_counts = counts.copy()
        for j in range(len(words)):
            start = i + j * word_length
            substring = s[start:start+word_length]
            if substring in curr_counts:
                curr_counts[substring] = curr_counts[substring] - 1
                if curr_counts[substring] == 0:
                    del curr_counts[substring]
            else:
                break
                
        if not curr_counts:
            indexes.add(i)
                
    return list(indexes)