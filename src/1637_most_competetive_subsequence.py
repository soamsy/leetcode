def mostCompetitive(nums: list[int], k: int) -> list[int]:
    stack = []
    for i, a in enumerate(nums):
        num_left = len(nums) - i
        while stack and stack[-1] > a and len(stack) - 1 + num_left >= k:
            stack.pop()
        if len(stack) < k:
            stack.append(a)
    return stack