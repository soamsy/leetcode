def numDecodings(s: str) -> int:
    if len(s) == 1:
        return 0 if 0 == int(s) else 1
    
    def validSingle(i):
        return s[i] != "0"
    def validDouble(i):
        return s[i] != "0" and int(s[i:i+2]) <= 26
    
    dp = [0] * len(s)
    dp[-1] = 1 if validSingle(len(s) - 1) else 0
    dp[-2] = 1 if validDouble(len(s) - 2) else 0
    dp[-2] += dp[-1] if validSingle(len(s) - 2) else 0
    
    for i in range(len(s) - 3, -1, -1):
        if s[i] != 0:
            dp[i] += dp[i+1] if validSingle(i) else 0
            dp[i] += dp[i+2] if validDouble(i) else 0
    
    return dp[0]