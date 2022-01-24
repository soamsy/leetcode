def findBestValue(arr: list[int], target: int) -> int:
    low = 0
    high = max(arr)
    
    closest_diff = target
    best_value = 0
    
    while low <= high:
        mid = (low + high) // 2
        total = sum([min(x, mid) for x in arr])
        
        diff = abs(total - target)
        if diff < closest_diff or diff == closest_diff and mid < best_value:
            closest_diff = diff
            best_value = mid
            
        if total < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return best_value