def longestPalindrome(s):
    longest = ""
    def checkSeq(seq):
        nonlocal longest
        if len(seq) > len(longest):
            longest = seq
        
    for i in range(0, len(s)):
        count = 0
        for j in range(1, (len(s) // 2) + 1):
            left = i - j
            right = i + j
            if left < 0 or right > len(s) - 1 or s[left] != s[right]:
                break
            count = j
        checkSeq(s[i - count:i + count + 1])
            
        count = 0
        for j in range(1, (len(s) // 2) + 1):
            left = i + 1 - j
            right = i + j
            if left < 0 or right > len(s) - 1 or s[left] != s[right]:
                break
            count = j
        checkSeq(s[i + 1 - count:i + count + 1])
            
            
                
    return longest
            


# print(longestPalindrome("babad"))
# print(longestPalindrome("bb"))