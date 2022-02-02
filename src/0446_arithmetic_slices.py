def numberOfArithmeticSlices(nums: list[int]) -> int:
    dp = [{} for _ in range(len(nums))]

    len_two_count = int(len(nums) * (len(nums) - 1) / 2)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            diff = nums[i] - nums[j]
            dp[j][diff] = dp[j].get(diff, 0) + 1

    for i in range(2, len(nums)):
        for j in range(0, i):
            diff = nums[j] - nums[i]
            if diff in dp[j]:
                dp[i][diff] = dp[i].get(diff, 0) + dp[j][diff]

    return sum([sum(m.values()) for m in dp]) - len_two_count

# print(numberOfArithmeticSlices([7,7,7,7,7]))
