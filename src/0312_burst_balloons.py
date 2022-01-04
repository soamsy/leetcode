def maxCoins(nums: list[int]) -> int:
    nums = [1] + nums + [1]
    cache = {}
    
    def sub(l, r):
        if l > r:
            return 0
        if (l, r) in cache:
            return cache[(l, r)]
        m = 0
        if len(set(nums[l-1:r+2])) == 1:
            return sum(map(lambda x: x**3, nums[l:r+1]))
        for i in range(l, r + 1):
            val = nums[i] * nums[l-1] * nums[r+1]
            val += sub(l,i-1)
            val += sub(i+1, r)
            m = max(val, m)
        cache[(l, r)] = m
        return m
            
            
    return sub(1, len(nums) - 2)