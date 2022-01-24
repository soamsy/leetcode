def replaceElements(arr: list[int]) -> list[int]:
    current_max = -1
    for i in range(len(arr) - 1, -1, -1):
        arr[i], current_max = current_max, max(current_max, arr[i])
    
    return arr