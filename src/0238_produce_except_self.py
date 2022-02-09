import itertools
import operator

def productExceptSelf(nums: list[int]) -> list[int]:
    prefix = [1] + list(itertools.accumulate([1, 2, 3], operator.mul))
    suffix = list(itertools.accumulate(nums[::-1], operator.mul))[::-1] + [1]
    
    return [prefix[i] * suffix[i+1] for i in range(len(nums))]

# print(productExceptSelf([1, 2, 3]))