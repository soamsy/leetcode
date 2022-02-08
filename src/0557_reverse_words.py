def reverseWords(s: str) -> str:
    return ' '.join([str(substr[::-1]) for substr in s.split()])