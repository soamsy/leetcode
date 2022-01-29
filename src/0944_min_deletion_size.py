def minDeletionSize(strs: list[str]) -> int:
    count = 0
    for col in zip(*strs):
        s = ''.join(col)
        if (s != ''.join(sorted(s))):
            count += 1
    return count