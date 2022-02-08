import itertools
def kIncreasing(arr: list[int], k: int) -> int:
    def lengthOfLIS(nums: List[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] <= x:
                sub.append(x)
            else:
                idx = bisect_right(sub, x)
                sub[idx] = x
        return len(sub)
                
    chunks = [arr[i:i+k] for i in range(0, len(arr), k)]
    result = 0
    for seq in itertools.zip_longest(*chunks, fillvalue=None):
        seq = list(filter(lambda x: x is not None, seq))
        result += len(seq) - lengthOfLIS(seq)
    return result