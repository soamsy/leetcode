def isAlienSorted(words: list[str], order: str) -> bool:
    rank = {}
    for i, letter in enumerate(order):
        rank[letter] = i
        
    def get_rank(a):
        return tuple([rank[c] for c in a])
        
    sorted_list = sorted(words, key=get_rank)
    return words == sorted_list