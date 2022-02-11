def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda i: i[0])
    
    r = []
    start = intervals[0][0]
    end = intervals[0][1]
    for i in intervals:
        if r and r[-1][1] >= i[0]:
            r[-1][1] = max(r[-1][1], i[1])
        else:
            r.append(i)
    
    return r