def fourSum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()

    quads = set()
    for a in range(0, len(nums) - 3):
        if nums[a] > target and nums[a] > 0:
            break
        for b in range(a + 1, len(nums) - 2):
            l = b + 1
            r = len(nums) - 1
            while l < r:
                quad = (nums[a], nums[b], nums[l], nums[r])
                val = sum(quad)
                if val == target:
                    quads.add(quad)
                    l += 1
                    r -= 1
                elif val < target:
                    l += 1
                else:
                    r -= 1
    return [list(x) for x in quads]