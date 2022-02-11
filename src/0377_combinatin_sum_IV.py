def combinationSum4(nums: list[int], target: int) -> int:
    comb = [0] * (target + 1)
    comb[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i - num >= 0:
                comb[i] += comb[i-num]
                
    return comb[target]