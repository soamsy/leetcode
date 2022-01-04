def maxArea(height: list[int]) -> int:
    i = 0
    j = len(height) - 1
    top_area = 0
    while i < j:
        top_area = max(top_area, (j - i) * min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return top_area


# giant_mountain = list(range(0, 10000)) + list(range(10000, -1, -1))
# print(maxArea(giant_mountain))


