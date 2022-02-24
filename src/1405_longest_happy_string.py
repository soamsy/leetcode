def longestDiverseString(a: int, b: int, c: int) -> str:
    counts = { 'a': a, 'b': b, 'c': c }
    for letter in ['a', 'b', 'c']:
        if counts[letter] == 0:
            del counts[letter]
    result = []
    def canPlaceLetter(letter):
        return len(result) < 2 or not (result[-1] == letter and result[-2] == letter)
    
    while counts:
        bySize = list(sorted(counts.items(), key = lambda x: x[1], reverse=True))
        validChoices = [(letter, count) for letter, count in bySize if canPlaceLetter(letter)]
        if not validChoices:
            break
        for letter, count in validChoices:
            result.append(letter)
            counts[letter] -= 1
            if counts[letter] == 0:
                del counts[letter]
            break
            
    return ''.join(result)