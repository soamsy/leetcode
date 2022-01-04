def isMatch(s: str, p: str) -> bool:
    def char_matches(sc, pc):
        return sc == pc or pc == '.'

    cache = {}
    def star_match(i, j):
        if i >= len(s) and j >= len(p):
            return True
        if j >= len(p):
            return False

        if (i, j) in cache:
            return cache[(i, j)]
        match = i < len(s) and char_matches(s[i], p[j])
        if j < len(p) - 1 and p[j+1] == '*':
            cache[(i, j)] = star_match(i, j+2) or (match and star_match(i+1, j))
            return cache[(i, j)]
        if match:
            cache[(i, j)] = star_match(i+1, j+1)
            return cache[(i, j)]

        cache[(i,j)] = False
        return False

    return star_match(0, 0)

# print(isMatch('aaaa', 'a*a*'))