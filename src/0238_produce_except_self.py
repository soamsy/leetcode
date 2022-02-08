import itertools

def productExceptSelf(nums: list[int]) -> list[int]:
    prefix = [1] + list(itertools.accumulate(nums, lambda a, b: a * b))
    suffix = list(itertools.accumulate(nums[::-1], lambda a, b: a * b))[::-1] + [1]
    
    return [prefix[i] * suffix[i+1] for i in range(len(nums))]