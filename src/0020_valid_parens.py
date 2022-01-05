def isValid(s: str) -> bool:
    open_to_close = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    
    close_to_open = {v: k for k, v in open_to_close.items()}
    
    stack = []
    
    for i in s:
        if i in open_to_close:
            stack.append(i)
        elif i in close_to_open:
            if len(stack) <= 0:
                return False
            last_open = stack.pop()
            if open_to_close[last_open] != i:
                return False
    
    return len(stack) == 0