def lastRemaining(n: int) -> int:
    left, right = 1, n
    start_left = True
    jump = 2
    while right - left >= jump:
        if right % jump == left % jump:
            right -= jump // 2
            left += jump // 2
        elif start_left:
            left += jump // 2
        else:
            right -= jump // 2
        jump *= 2
        start_left = not start_left
    
    return right if start_left else left