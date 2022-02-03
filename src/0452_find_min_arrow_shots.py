def findMinArrowShots(points: list[list[int]]) -> int:
    points.sort(key=lambda p: (p[0], p[1]))
    
    curr = [points[0][0], points[0][1]]
    total = 1
    for i in range(1, len(points)):
        p = points[i]
        if p[0] <= curr[1]:
            curr[0] = p[0]
            curr[1] = min(curr[1], p[1])
        else:
            total += 1
            curr = [p[0], p[1]]
    
    return total