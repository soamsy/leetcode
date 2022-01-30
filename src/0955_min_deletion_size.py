def minDeletionSize(strs: list[str]) -> int:
    needToCheck = set(range(len(strs)))
    count = 0
    for col in zip(*strs):
        pairs = [p for p in zip(col, col[1:])]
        if all([a <= b for i, (a, b) in enumerate(pairs) if i in needToCheck]):
            needToCheck -= {i for i, (a, b) in enumerate(pairs) if a < b}
            if not needToCheck:
                return count
        else:
            count += 1
    return count