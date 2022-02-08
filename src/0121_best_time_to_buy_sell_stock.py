def maxProfit(prices: list[int]) -> int:
    l, r = 0, 0
    max_profit = 0
    for i, p in enumerate(prices):
        if p < prices[l]:
            max_profit = max(max_profit, prices[r] - prices[l])
            l = i
            r = i
        elif p > prices[r]:
            r = i
            
    return max(max_profit, prices[r] - prices[l])