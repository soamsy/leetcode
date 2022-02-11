import collections
def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0
    uf = { x: x for x in nums }
    def find(x):
        if x != uf[x]:
            uf[x] = find(uf[x])
        return uf[x]
    
    for num in nums:
        if (num+1) in uf:
            a = find(num)
            b = find(num+1)
            if a != b:
                uf[find(num)] = find(num+1)
                
    return max(collections.Counter([find(x) for x in uf.keys()]).values())