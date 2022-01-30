import math

def largestComponentSize(nums: list[int]) -> int:
    nums.sort()
    uf = {}
    sizes = {}
    for num in nums:
        uf[num] = num
        sizes[num] = 1
    
    def find(x):
        if x not in uf:
            uf[x] = x
            sizes[x] = 0
            
        is_root = uf[x] == x
        if not is_root:
            uf[x] = find(uf[x])
        return uf[x]
    
    def merge(a, b):
        rootA = find(a)
        rootB = find(b)
        if rootA == rootB:
            return
        
        if sizes[rootA] > sizes[rootB]:
            rootA, rootB = rootB, rootA
        uf[rootA] = rootB
        sizes[rootB] += sizes[rootA]
    
    max_num = nums[-1]
    for f in itertools.takewhile(lambda x: x <= math.sqrt(max_num), range(2, max_num)):
        for num in nums:
            if num % f == 0 and f <= math.sqrt(num):
                merge(num, f)
                merge(num, num // f)
    
    return max(sizes.values())