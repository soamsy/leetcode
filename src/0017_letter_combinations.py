def letterCombinations(digits: str) -> list[str]:
    digitToLetters = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }
    
    letters = list(map(lambda x: digitToLetters[int(x)], digits))
    
    def combinations(i):
        if i > len(letters) - 1:
            return []
        if i == len(letters) - 1:
            return letters[i]
            
        seqs = combinations(i+1)
        new_seqs = []
        for c in letters[i]:
            new_seqs = new_seqs + [c + x for x in seqs]
        return new_seqs
                
        
    return combinations(0)