def threeSum(nums: list[int]) -> list[list[int]]:
    triplets = set()
    nums.sort()
    for i in range(0, len(nums) - 2):
        if nums[i] > 0:
            break
            
        left = i + 1
        right = len(nums) - 1
        while left < right:
            val = nums[i] + nums[left] + nums[right]
            if val < 0:
                left += 1
            elif val > 0:
                right -= 1
            else:
                triplets.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
                
    return [list(x) for x in triplets]