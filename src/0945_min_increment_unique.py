def minIncrementForUnique(nums: list[int]) -> int:
    max_num = max(nums)
    counts = [0] * (max_num + 1)
    for n in nums:
        counts[n] += 1
    
    carryover = 0
    moves = 0
    for c in counts:
        moves += carryover
        carryover = max(carryover + (c - 1), 0)
    
    moves += sum(range(carryover + 1))
    
    return moves