def findMaxLength(nums: list[int]) -> int:
    off_by_seq = [0] * len(nums)
    for i, num in enumerate(nums):
        off_by_seq[i] = (off_by_seq[i-1] if i != 0 else 0) + (1 if num == 1 else -1)
        
    indexes = { c: i for i, c in enumerate(off_by_seq) }
    
    max_distance = 0
    for i, offby in enumerate(off_by_seq):
        best_length = indexes[offby] - i if offby != 0 else i + 1
        max_distance = max(max_distance, best_length)

    return max_distance