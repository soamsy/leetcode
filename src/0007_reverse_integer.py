def reverse(x: int) -> int:
    negative = -1 if x < 0 else 1
    x = abs(x)
    digits = [i for i in str(x)][::-1]
    r = int(''.join(digits))
    if r < -(2**31) or (2**31 - 1) < r:
        return 0;
    return r * negative

# print(reverse(321))