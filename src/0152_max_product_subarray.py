def maxProduct(nums: list[int]) -> int:
    max_pos = nums[:]
    max_neg = nums[:]
    
    for i in range(1, len(nums)):
        max_pos[i] = max(max_pos[i], max_pos[i-1] * nums[i], max_neg[i-1] * nums[i])
        max_neg[i] = min(max_neg[i], max_pos[i-1] * nums[i], max_neg[i-1] * nums[i])
    
    return max(max_pos)