def reverseStr(s: str, k: int) -> str:
    chunks = [s[i:i+k] for i in range(0, len(s), k)]
    result = ""
    for i, chunk in enumerate(chunks):
        result += ''.join(chunk[::-1] if i % 2 == 0 else chunk)
    return result