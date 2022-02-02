def findDuplicates(nums: list[int]) -> list[int]:
    i = 0
    result = set()
    while i < len(nums):
        target = nums[i] - 1
        if nums[i] == nums[target]:
            if nums[i] != i + 1:
                result.add(nums[i])
            i += 1
        else:
            nums[i], nums[target] = nums[target], nums[i]
            
    return list(result)