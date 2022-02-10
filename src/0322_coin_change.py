def coinChange(coins: list[int], amount: int) -> int:
    dp = [[-1] * len(coins) for _ in range(amount + 1)]
    
    for c in range(len(coins)):
        dp[0][c] = 0
        
    for total in range(1, amount + 1):
        for c in range(len(coins)):
            coin = coins[c]
            if total-coin >= 0:
                best = min([x for x in dp[total-coin] if x != -1], default=-1)
                if best != -1:
                    dp[total][c] = best + 1
    
    return min([x for x in dp[amount] if x != -1], default=-1)