import bisect
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    def intersects(a, b):
        if a[0] > b[0]:
            a, b = b, a
        return a[0] <= b[0] <= a[1]
        
    index = bisect.bisect_left(intervals, newInterval[0], key=lambda i: i[0])
    back = 0
    forward = 0
    while 0 <= index - back - 1 and intersects(intervals[index - back - 1], newInterval):
        back += 1
        
    while index + forward < len(intervals) and intersects(newInterval, intervals[index + forward]):
        forward += 1
    
    left, right = newInterval
    if back > 0 or forward > 0:
        left = min(left, intervals[index - back][0])
        right = max(right, intervals[index + forward - 1][1])
        
    intervals = [p for i, p in enumerate(intervals) if not (index - back <= i < index + forward)]
    intervals.insert(index - back, [left, right])
    return intervals