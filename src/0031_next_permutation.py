def nextPermutation(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def reverse(nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
    if not nums:
        return
    
    a = None
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            a = i
            break
    
    if a is None:
        reverse(nums, 0, len(nums) - 1)
        return
    
    b = None
    for i in range(len(nums) - 1, a, -1):
        if nums[a] < nums[i]:
            b = i
            break

    nums[a], nums[b] = nums[b], nums[a]
    reverse(nums, a+1, len(nums) - 1)