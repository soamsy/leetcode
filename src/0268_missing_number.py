def missingNumber(nums: list[int]) -> int:
    nonMissingTotal = int(len(nums) * (len(nums) + 1) / 2)
    return nonMissingTotal - sum(nums)