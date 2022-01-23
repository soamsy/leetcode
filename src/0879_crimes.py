def profitableSchemes(n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
    total_schemes = len(group)
    dp = [[[0] * (minProfit+1) for _ in range(n+1)] for _ in range(total_schemes+1)]
    
    for members in range(n+1):
        dp[0][members][0] = 1
        
    for scheme in range(1, total_schemes + 1):
        g = group[scheme - 1]
        p = profit[scheme - 1]
        for member in range(n+1): 
            for reward in range(minProfit+1): 
                dp[scheme][member][reward] += dp[scheme-1][member][reward]
                if g <= member:
                    dp[scheme][member][reward] += dp[scheme-1][member-g][max(0, reward-p)]
    
    return dp[total_schemes][n][minProfit] % (10**9 + 7)