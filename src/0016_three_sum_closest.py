def threeSumClosest(nums: list[int], target: int) -> int:
    nums.sort()
    closest = float("infinity")
    
    for i in range(0, len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            val = nums[i] + nums[left] + nums[right]
            if abs(val - target) < abs(closest - target):
                closest = val
            if val < target:
                left += 1
            elif target < val:
                right -= 1
            else:
                return closest
    return closest