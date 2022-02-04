def minMoves2(nums: list[int]) -> int:
    nums.sort()
    mid = len(nums) // 2
    median = nums[mid]
    return sum([abs(n - median) for n in nums])