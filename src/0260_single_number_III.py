import functools
def singleNumber(nums: list[int]) -> list[int]:
    diff = functools.reduce(lambda a, b: a ^ b, nums)
    bit = diff & -diff
    result = [0, 0]
    for n in nums:
        if bit & n == bit:
            result[0] ^= n
        else:
            result[1] ^= n
    
    return result