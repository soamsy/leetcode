import itertools

def decompressRLElist(nums: list[int]) -> list[int]:
    chunks = [nums[i:i+2] for i in range(0, len(nums), 2)]
    return itertools.chain(*[itertools.repeat(val, freq) for freq, val in chunks])