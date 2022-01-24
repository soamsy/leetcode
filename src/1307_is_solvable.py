import itertools

def isSolvable(words: list[str], result: str) -> bool:
    start_letters = set()
    
    def collect_no_zeros(w):
        if len(w) > 1:
            start_letters.add(w[0])
            
    collect_no_zeros(result)
    for w in words:
        collect_no_zeros(w)
    
    result = result[::-1]
    for i in range(len(words)):
        words[i] = words[i][::-1]
        
    levels = list(itertools.zip_longest(result, *words))
    digits = set(range(0,10))
    
    mapping = {}
    
    def toNum(w):
        return int(''.join([str(mapping[c]) for c in w]))
    
    def fn(level, remainder, used):
        if level == len(levels):
            if remainder == 0:
                return True
            else:
                return False
        
        chars_at_level = set([c for c in levels[level] if c is not None])
        needy_chars = [c for c in chars_at_level if c not in mapping]
        
        available_digits = digits - used
        
        for seq in itertools.permutations(available_digits, len(needy_chars)):
            invalid_zeros = [v for i, v in enumerate(seq) if v == 0 and needy_chars[i] in start_letters]
            if invalid_zeros:
                continue
                
            for i, v in enumerate(seq):
                mapping[needy_chars[i]] = v
            
            lhs = sum([toNum(w[level::-1]) for w in words])
            rhs = toNum(result[level::-1])
            lhs_up_to_level = lhs % 10**(level + 1)
            if lhs_up_to_level == rhs:
                if fn(level + 1, lhs - lhs_up_to_level, set.union(used, set(seq))):
                    return True
                
            for i, _ in enumerate(seq):
                del mapping[needy_chars[i]]
            
        return False
    
    return fn(0, 0, set())