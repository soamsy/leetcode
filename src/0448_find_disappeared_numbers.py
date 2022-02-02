def findDisappearedNumbers(nums: list[int]) -> list[int]:
    arr = [None] * len(nums)
    
    for num in nums:
        arr[num-1] = num
    
    return [i+1 for i, v in enumerate(arr) if v is None]