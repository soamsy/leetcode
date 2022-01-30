import collections
def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    q = collections.deque(nums)
    for i in range(k):
        q.appendleft(q.pop())
    
    for i in range(len(q)):
        nums[i] = q[i]