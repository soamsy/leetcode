def frequencySort(s: str) -> str:
    count = collections.Counter(s)
    return ''.join(list(sorted(s, key=lambda c: (-count[c], c))))