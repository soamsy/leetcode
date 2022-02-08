def nextGreaterElements(nums: list[int]) -> list[int]:
    stack = []
    
    result = [-1] * len(nums)
    for i, n in enumerate(nums):
        while stack and nums[stack[-1]] < n:
            result[stack.pop()] = n
        stack.append(i)
        
    for i, n in enumerate(nums):
        while stack and nums[stack[-1]] < n:
            result[stack.pop()] = n
            
    return result