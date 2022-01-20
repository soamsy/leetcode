def firstMissingPositive(nums: list[int]) -> int:
    i = 0
    while i < len(nums):
        n = nums[i]
        if 0 < n and n <= len(nums) and i != n - 1 and nums[i] != nums[n-1]:
            nums[i], nums[n-1] = nums[n-1], nums[i]
        else:
            i += 1
    
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
        
    return len(nums) + 1