def nextGreaterElement(n: int) -> int:
    digits = list(reversed([int(d) for d in str(n)]))
    result = None
    for i in range(len(digits) - 1):
        if digits[i] > digits[i+1]:
            toSwap = 0
            while digits[toSwap] <= digits[i+1]:
                toSwap += 1
            digits[toSwap], digits[i+1] = digits[i+1], digits[toSwap]
            result = digits[0:i+1][::-1] + digits[i+1:len(digits)]
            break
            
    if result is None:
        return -1
    total = int(''.join([str(x) for x in result[::-1]]))
    if total >= 2**31:
        return -1
    else:
        return total