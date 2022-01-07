def divide(dividend: int, divisor: int) -> int:
    def negate(n):
        result = n
        result -= n
        result -= n
        return result
    
    def multiply(n, k):
        if n < k:
            n, k = k, n
        total = 0
        for i in range(k):
            total += n
        return total
    
    def simple_div(top, bottom, k=1, count=0):
        t = top
        b = multiply(bottom, k)
        while t >= b:
            t -= b
            count += k
        return (t, count)
    
    def div(top, bottom):
        positive = (top >= 0 and bottom >= 0) or (top < 0 and bottom < 0)
        if top < 0:
            top = negate(top)
        if bottom < 0:
            bottom = negate(bottom)
            
        magnitude_diff = len(str(top)) - len(str(bottom))
        ks = [1]
        if magnitude_diff > 1:
            accumulate = 10
            for i in range(magnitude_diff):
                ks.append(accumulate)
                accumulate = multiply(accumulate, 10)
                
        ks = ks[::-1]
        count = 0
        remainder = top
        for k in ks:
            remainder, count = simple_div(remainder, bottom, k, count)

        return count if positive else negate(count)
    
    
    val = div(dividend, divisor)
    return max(-2147483648, min(val, 2147483647))