def countArrangement(n: int) -> int:
    options = [[] * n for _ in range(n)]
    for i in range(1, n + 1):
        for j in range(1, i):
            if i % j == 0:
                options[i-1].append(j)
        for j in range(i, n+1, i):
            options[i-1].append(j)
    
    options.sort(key=len)
    
    taken = set()
    def backtrack(i):
        if i >= n:
            return 1
        
        total = 0
        for option in [o for o in options[i] if o not in taken]:
            taken.add(option)
            total += backtrack(i+1)
            taken.remove(option)
        return total
                
    return backtrack(0)