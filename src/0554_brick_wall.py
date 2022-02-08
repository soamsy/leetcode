import collections
def leastBricks(wall: list[list[int]]) -> int:
    counts = collections.defaultdict(int)
    for row in wall:
        total = 0
        for brick in row[:-1]:
            total += brick
            counts[total] += 1
    
    
    return len(wall) - max(counts.values(), default=0)