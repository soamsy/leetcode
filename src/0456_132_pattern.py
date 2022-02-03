def find132pattern(nums: list[int]) -> bool:
    stack = []
    nums = nums[::-1]
    
    bar = float("-infinity")
    for num in nums:
        if num < bar:
            return True
        while stack and num > stack[-1]:
            bar = stack.pop()
        stack.append(num)
    
    return False