def lengthOfLIS(nums: list[int]) -> int:
    dp = [1] * len(nums)
    for i in range(len(nums)):
        dp[i] = max(dp[i], max([dp[j] + 1 for j in range(i) if nums[j] < nums[i]], default=0))
    return max(dp)