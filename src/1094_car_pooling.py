def carPooling(trips: list[list[int]], capacity: int) -> bool:
    spots = {}
    for trip in trips:
        for i in range(trip[1], trip[2]):
            spots[i] = trip[0] + spots.get(i, 0)
    max_needed = max(spots.values())
    return capacity >= max_needed