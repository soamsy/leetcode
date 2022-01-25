def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    right = 0
    longest = 0
    last_location = {}
    while right < len(s):
        if s[right] in last_location:
            left = max(last_location[s[right]] + 1, left)
            del last_location[s[right]]
        else:
            last_location[s[right]] = right
            right += 1
            longest = max(longest, right - left)
    return longest