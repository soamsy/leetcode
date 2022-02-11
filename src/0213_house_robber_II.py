from functools import cache
def rob(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]

    @cache
    def fn(i, skips, limit):
        if i >= n:
            return 0
        
        if i >= limit:
            return 0
        
        if skips == 2:
            return nums[i] + fn(i+1, 0, limit)
        elif skips == 1:
            return max(nums[i] + fn(i+1, 0, limit), fn(i+1, 2, limit))
        else:
            return fn(i+1, 1, limit)
    
    ignoreEnds = fn(1, 2, n - 1)
    takeFirst = nums[0] + fn(1, 0, n - 1)
    takeLast = nums[-1] + fn(1, 1, n - 2)
    
    return max(ignoreEnds, takeFirst, takeLast)