import re
def findMinDifference(timePoints: list[str]) -> int:
    def toMinutes(s):
        parsed = re.findall('(\d\d):(\d\d)', s)
        return int(parsed[0][0]) * 60 + int(parsed[0][1])
    
    max_mins = 24 * 60
    mins = [toMinutes(tp) for tp in timePoints]
    
    mins.sort()
    min_diff = float("infinity")
    for m1, m2 in zip(mins, mins[1:]):
        min_diff = min(min_diff, m2 - m1)
    min_diff = min(min_diff, max_mins - mins[-1] + mins[0])
    return min_diff