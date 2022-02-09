def search(nums: list[int], target: int) -> int:
    if not nums:
        return -1
    
    searchLeft = nums[0] <= target
    
    left, right = 0, len(nums) - 1
    while left <= right:
        m = (left + right) // 2
        if nums[m] == target:
            return m
        
        inLeft = nums[0] <= nums[m]
        inTargetArray = searchLeft == inLeft
        if (inTargetArray and nums[m] < target) or (not inTargetArray and inLeft):
            left = m + 1
        else:
            right = m - 1
        
    return -1