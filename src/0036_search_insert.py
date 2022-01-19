def searchInsert(nums: list[int], target: int) -> int:
    def binary(left, right):
        if left > right:
            return left
        m = (left + right) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            return binary(m + 1, right)
        else:
            return binary(left, m - 1)
    return binary(0, len(nums) - 1)