def carPooling(trips: list[list[int]], capacity: int) -> bool:
    spots = [0] * 1001
    for trip in trips:
        spots[trip[1]] += trip[0]
        spots[trip[2]] -= trip[0]
    
    needed = 0
    for i in spots:
        needed += i
        if needed > capacity:
            return False
    return True