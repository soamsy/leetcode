def minMoves(nums: list[int]) -> int:
    lowest = min(nums)
    return sum([x - lowest for x in nums])