def minInsertions(s: str) -> int:
    dp = [[0] * len(s) for _ in range(len(s))]
    
    for left in range(len(s) - 1, -1, -1):
        for right in range(0, len(s)):
            if left >= right:
                continue
            if s[left] == s[right]:
                dp[left][right] = dp[left+1][right-1]
            else:
                dp[left][right] = 1 + min(dp[left+1][right], dp[left][right-1])
    
    return dp[0][len(s) - 1]