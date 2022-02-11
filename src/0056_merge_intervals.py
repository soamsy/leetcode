def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda i: i[0])
    
    result = []
    start = intervals[0][0]
    end = intervals[0][1]
    for i in intervals:
        if end >= i[0]:
            end = max(end, i[1])
        else:
            result.append([start, end])
            start = i[0]
            end = i[1]
    result.append([start, end])
    
    return result