def bagOfTokensScore(tokens: list[int], power: int) -> int:
    tokens.sort()
    i = 0
    j = len(tokens) - 1
    score = 0
    max_score = 0
    while i <= j and (tokens[i] <= power or score > 0):
        while i <= j and tokens[i] <= power:
            power -= tokens[i]
            i += 1
            score += 1
            max_score = max(max_score, score)
            
        while i <= j and score > 0 and tokens[i] > power:
            power += tokens[j]
            score -= 1
            j -= 1
    
    return max_score