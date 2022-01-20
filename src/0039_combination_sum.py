def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    solutions = set()
    checked = set()
    stack = []
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
            for i in candidates:
                stack.append(i)
                recur(total + i)
                stack.pop()
                
    recur(0)
    return [list(x) for x in solutions]