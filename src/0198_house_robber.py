from functools import cache
def rob(nums: list[int]) -> int:
    n = len(nums)
    
    @cache
    def fn(i, numSkipped):
        if i >= n:
            return 0
        
        if numSkipped == 2:
            return nums[i] + fn(i + 1, 0)
        elif numSkipped == 1:
            return max(fn(i+1, 2), nums[i] + fn(i+1, 0))
        else:
            return fn(i+1, 1)
    
    return fn(0, 1)