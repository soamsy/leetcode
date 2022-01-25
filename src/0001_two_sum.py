def twoSum(nums: list[int], target: int) -> list[int]:
    pairs = {}
    for i in range(len(nums)):
        pairs[target - nums[i]] = i
    for i in range(len(nums)):
        pair = pairs.get(nums[i])
        if pair and i != pair:
            return [i, pair]