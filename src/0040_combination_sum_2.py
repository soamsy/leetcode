def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    solutions = set()
    checked = set()
    stack = []
    
    freq = {}
    for i in candidates:
        freq[i] = freq.get(i, 0) + 1
        
    def recur(total):
        seq = tuple(sorted(stack[:]))
        if seq in checked:
            return

        checked.add(seq)
        if total == target:
            solutions.add(seq)
            return
        elif total > target:
            return
        else:
            keys = list(freq.keys())
            for i in keys:
                stack.append(i)
                freq[i] -= 1
                if freq[i] == 0:
                    del freq[i]
                recur(total + i)
                freq[i] = freq.get(i, 0) + 1
                stack.pop()

    recur(0)
    return [list(x) for x in solutions]