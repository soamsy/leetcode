import math
def minEatingSpeed(piles: list[int], h: int) -> int:
    if h < len(piles):
        return -1
    
    min_hours = [1] * len(piles)
    max_hours = min_hours[:]
    hours_left = h - len(piles)
    total = sum(piles)
    for b in range(len(piles)):
        min_hours[b] += (math.floor(hours_left * piles[b] / total))
        max_hours[b] += (math.ceil(hours_left * piles[b] / total))
    overshoot_k = map(lambda p, h: math.ceil(p / h), piles, min_hours)
    needed_k = map(lambda p, h: math.ceil(p / h), piles, max_hours)
    
    low_k = max(needed_k)
    high_k = max(overshoot_k)
    
    current_k = high_k
    while low_k <= high_k:
        mid = (low_k + high_k) // 2
        piles_consumed = 0
        hours_left = h
        for i in range(len(piles)):
            hours_needed = math.ceil(piles[i] / mid)
            if hours_needed <= hours_left:
                piles_consumed += 1
                hours_left -= hours_needed
            else:
                break
        if piles_consumed == len(piles):
            if mid < current_k:
                current_k = mid
                high_k = mid - 1
            else:
                low_k = mid + 1
        else:
            low_k = mid + 1
    
    return current_k