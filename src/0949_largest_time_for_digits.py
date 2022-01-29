import itertools
import itertools
def largestTimeFromDigits(arr: list[int]) -> str:
    def valid(p):
        return p[:2] < (2, 4) and p[2] < 6
    
    max_time = -1
    max_perm = []
    for perm in itertools.permutations(arr, len(arr)):
        if valid(perm):
            time = int(''.join([str(p) for p in perm]))
            if max_time < time:
                max_time = time
                max_perm = perm
            
    if not max_perm:
        return ""
    clock_time = ''.join([str(d) for d in max_perm])
    return clock_time[0:2] + ":" + clock_time[2:4]