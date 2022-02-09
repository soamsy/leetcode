def findMin(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        if nums[left] <= nums[right]:
            return nums[left]
        
        mid = (left + right) // 2
        if mid != 0 and nums[mid - 1] > nums[mid]:
            return nums[mid]
        elif nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid - 1
    
    return -10000