import re
def isPalindrome(s: str) -> bool:
    s = re.sub("[^a-zA-Z0-9]", "", s).lower()
    return s == ''.join(list(reversed(s)))