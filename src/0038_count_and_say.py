def countAndSay(n: int) -> str:
    def parse(digits):
        count = 1
        after = digits[-1]
        pos = len(digits) - 2
        for pos in range(len(digits) -2, -1, -1):
            if (digits[pos] == after[0]):
                count += 1
            else:
                after = digits[pos] + str(count) + after
                count = 1
        return str(count) + after
                
    
    def recur(n):
        if n == 1:
            return "1"
        return parse(recur(n - 1))
    
    return recur(n)