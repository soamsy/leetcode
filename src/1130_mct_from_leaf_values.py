import functools
def mctFromLeafValues(arr: list[int]) -> int:
    increasing = list(sorted([(v, i) for i, v in enumerate(arr)]))
    
    uf = {i: i for i in range(len(arr))}
    
    def find(i):
        if i < 0 or i >= len(arr):
            return None
        if i != uf[i]:
            uf[i] = find(uf[i])
        return uf[i]
    
    total = 0
    for value, i in increasing:
        myRoot = find(i)
        right = i + 1
        toMerge = []
        while find(right) == myRoot and right < len(arr):
            right += 1
        if right < len(arr):
            toMerge.append(find(right))
        left = i - 1
        while find(left) == myRoot and left >= 0:
            left -= 1
        if left >= 0:
            toMerge.append(find(left))
        
        if toMerge:
            bestRoot = list(sorted(toMerge, key=lambda x: arr[x]))[0]
            total += arr[bestRoot] * arr[myRoot]
            if arr[bestRoot] > arr[myRoot]:
                uf[myRoot] = bestRoot
            else:
                uf[bestRoot] = myRoot
        
    return total