def carPooling(trips: list[list[int]], capacity: int) -> bool:
    spots = [0] * 1001
    for trip in trips:
        spots[trip[1]] += trip[0]
        spots[trip[2]] -= trip[0]
    
    needed = 0
    for spot in spots:
        needed += spot
        if needed > capacity:
            return False
    return True