def validMountainArray(arr: list[int]) -> bool:
    if len(arr) < 3:
        return False
    
    i = 1
    while i < len(arr):
        if arr[i-1] < arr[i]:
            i += 1
        elif arr[i-1] == arr[i]:
            return False
        else:
            break
    
    if i == len(arr) or i == 1:
        return False
    
    while i < len(arr):
        if arr[i-1] > arr[i]:
            i += 1
        else:
            return False
    return True