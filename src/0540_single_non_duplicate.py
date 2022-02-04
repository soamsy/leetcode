def singleNonDuplicate(nums: list[int]) -> int:
    def isLeftDup(i):
        return (nums[i] == nums[i-1]) if i > 0 else False
    
    def isRightDup(i):
        return (nums[i] == nums[i+1]) if i < len(nums) - 1 else False
    
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        left = isLeftDup(mid)
        right = isRightDup(mid)
        if not left and not right:
            return nums[mid]
        
        shouldBeEven = mid + 1 if left else mid
        if shouldBeEven % 2 == 0:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1