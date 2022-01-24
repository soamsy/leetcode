def canReach(arr: list[int], start: int) -> bool:
    traversed = [False] * len(arr)
    q = collections.deque([start])
    while q:
        loc = q.pop()
        if loc < 0 or loc >= len(arr):
            continue
        if traversed[loc]:
            continue
        if arr[loc] == 0:
            return True
        
        traversed[loc] = True
        
        dist = arr[loc]
        q.append(loc + dist)
        q.append(loc - dist)
    
    return False