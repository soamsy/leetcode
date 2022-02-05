def relativeSortArray(arr1: list[int], arr2: list[int]) -> list[int]:
    indexes = { c: i for i, c in enumerate(arr2) }
    arr1.sort(key=lambda x: indexes[x] if x in indexes else len(indexes) + x)
    return arr1