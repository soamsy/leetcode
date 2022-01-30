import itertools
import collections

def canReorderDoubled(arr: list[int]) -> bool:
    arr.sort()
    neg = list(itertools.takewhile(lambda x: x <= 0, arr))
    arr = arr[len(neg):]
    zeros = []
    while neg and neg[-1] == 0:
        zeros.append(neg.pop())
    
    def fn(xs):
        count = collections.Counter(xs)
        for x in xs:
            if count[x] == 0:
                continue
            if count[x * 2] > 0:
                count[x] -= 1
                count[x * 2] -= 1
            else:
                return False
        
        return all([c == 0 for c in count.values()])
    
    return fn(arr) and fn(list(reversed(neg))) and len(zeros) % 2 == 0