def search(nums: list[int], target: int) -> int:
    if not nums:
        return -1
    
    first = nums[0]
    search_left = first <= target
    def binary(left, right):
        def in_array_search():
            if middle < target:
                return binary(m + 1, right)
            else:
                return binary(left, m - 1)
        
        if left > right:
            return -1
        m = right - left // 2
        middle = nums[m]
        if middle == target:
            return m
        in_left = middle >= first
        if search_left:
            if in_left:
                return in_array_search()
            else:
                return binary(left, m - 1)
        else:
            if in_left:
                return binary(m + 1, right)
            else:
                return in_array_search()
    
    return binary(0, len(nums) - 1)