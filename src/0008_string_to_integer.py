def myAtoi(s: str) -> int:
    import re
    s = s.strip()
    matches = re.findall("^([+-]?)(\d+).*", s)
    if len(matches) == 0:
        return 0
    negative = -1 if matches[0][0] == "-" else 1
    num = int(matches[0][1])
    return min(2**31-1, max(-(2**31), negative * num))