def canJump(nums: list[int]) -> bool:
    max_index = 0
    for i, num in enumerate(nums):
        if i > max_index:
            return False
        max_index = max(max_index, num+i)
        if max_index >= len(nums):
            return True
    return True