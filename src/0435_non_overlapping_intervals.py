def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda i: i[1])
    
    toDelete = 0
    i = 0
    while i < len(intervals):
        bestEndBoundary = intervals[i][1]
        j = i + 1
        while j < len(intervals) and intervals[j][0] < bestEndBoundary:
            j += 1
        toDelete += (j - i - 1)
        i = j
        
    return toDelete