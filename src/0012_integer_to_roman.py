def intToRoman(num: int) -> str:
    digits = [int(x) for x in str(num)][::-1]
    digits = digits + [0] * (4 - len(digits))
    
    def toRoman(x, one_char, five_char, ten_char):
        if x == 0:
            return ''
        elif 1 <= x <= 3:
            return one_char * x
        elif x == 4:
            return one_char + five_char
        elif x == 5:
            return five_char
        elif 6 <= x <= 8:
            return five_char + (one_char * (x - 5))
        elif x == 9:
            return one_char + ten_char
    reversed_roman = list(map(toRoman, digits, ['I', 'X', 'C', 'M'], ['V', 'L', 'D', ''], ['X', 'C', 'M', '']))
    return ''.join(reversed_roman[::-1])