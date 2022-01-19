def longestValidParentheses(s: str) -> int:
    stack = []
    ranges = []
    for i in range(len(s)):
        if s[i] == ')' and stack:
            opening = stack.pop()
            ranges.append((opening, i))
        elif s[i] == '(':
            stack.append(i)
    
    if not ranges:
        return 0
    ranges.sort(key=lambda r: r[0])
    i = 0
    for i in range(len(ranges) - 1):
        a = ranges[i]
        b = ranges[i + 1]
        if b[1] < a[1] or a[1] + 1 == b[0]:
            ranges[i + 1] = (a[0], max(a[1], b[1]))
            ranges[i] = None
            
    
    max_range = max([r for r in ranges if r], key=lambda r: r[1] - r[0])
            
    return max_range[1] - max_range[0] + 1