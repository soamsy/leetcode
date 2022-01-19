def searchRange(nums: list[int], target: int) -> list[int]:
    def search_left(left, right):
        if left > right:
            return -1
        print(f"left: {left} right: {right}")
        m = (right + left) // 2
        middle = nums[m]
        if middle == target and (m <= 0 or nums[m - 1] != target):
            return m
        elif middle == target:
            return search_left(left, m - 1)
        else:
            return search_left(m + 1, right)
    
    def search_right(left, right):
        if left > right:
            return -1
        m = (right + left) // 2
        middle = nums[m]
        if middle == target and (m >= len(nums) - 1 or nums[m + 1] != target):
            return m
        elif middle == target:
            return search_right(m + 1, right)
        else:
            return search_right(left, m - 1)
        
    def binary(left, right):
        if left > right:
            return [-1, -1]
        m = (right + left) // 2
        middle = nums[m]
        if middle == target:
            return [search_left(left, m), search_right(m, right)]
        if middle < target:
            return binary(m + 1, right)
        else:
            return binary(left, m - 1)
    return binary(0, len(nums) - 1)