import collections
def findPairs(nums: list[int], k: int) -> int:
    if k == 0:
        return sum([1 for k, c in collections.Counter(nums).items() if c > 1])
    
    nums = list(sorted(set(nums)))
    indexes = { c: i for i, c in enumerate(nums)}
    total = 0
    for num in nums:
        if num + k in indexes:
            total += 1
        
    return total