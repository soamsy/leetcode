from functools import cache
def tallestBillboard(rods: list[int]) -> int:
    n = len(rods)
    max_height = sum(rods) // 2
    
    @cache
    def fn(target, i):
        if abs(target) > max_height:
            return None
        
        if i >= n:
            if target == 0:
                return 0
            else:
                return None
            
        left = fn(target + rods[i], i+1)
        if left is not None:
            left += rods[i]
            
        right = fn(target - rods[i], i+1)
        if right is not None:
            right += rods[i]
        
        unused = fn(target, i+1)
        
        validPaths = [total for total in [left, right, unused] if total is not None]
        
        if validPaths:
            return max(validPaths)
        else:
            return None
        
        
    result = fn(0, 0)
    return result // 2 if result is not None else 0