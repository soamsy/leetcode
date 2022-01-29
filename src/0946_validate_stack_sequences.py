def validateStackSequences(pushed: list[int], popped: list[int]) -> bool:
    stack = []
    popped = popped[::-1]
    for p in pushed:
        stack.append(p)
        while stack and popped and stack[-1] == popped[-1]:
            stack.pop()
            popped.pop()
        
    return len(popped) == 0