from functools import cache

def removeBoxes(boxes: list[int]) -> int:
    @cache
    def fn(i, j, k):
        if i > j:
            return k**2
        
        scan = i
        while scan <= j and boxes[i] == boxes[scan]:
            scan += 1
        
        total_same = scan - i + k
        if scan > j:
            return total_same**2
        
        distant_but_same = []
        next_i = scan
        while next_i <= j:
            if boxes[next_i] == boxes[i]:
                distant_but_same.append(next_i)
            next_i += 1
            
        take_now = total_same**2 + fn(scan, j, 0)
        if distant_but_same:
            highest = take_now
            for distant in distant_but_same:
                highest = max(highest, fn(scan, distant - 1, 0) + fn(distant, j, total_same))
            return highest
        else:
            return take_now
        
        
    return fn(0, len(boxes) - 1, 0)