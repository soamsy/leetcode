def romanToInt(s: str) -> int:
    import re
    regex = "^(M*)([CDM]*)([XLC]*)([IVX]*)$"
    roman_1000, roman_100, roman_10, roman_1 = re.findall(regex, s)[0]
    
    def createRomanMap(one_c, five_c, ten_c):
        return {
            one_c: 1,
            one_c * 2: 2,
            one_c * 3: 3,
            one_c + five_c: 4,
            five_c: 5,
            five_c + one_c: 6,
            five_c + one_c * 2: 7,
            five_c + one_c * 3: 8,
            one_c + ten_c: 9
        }
    
    ones = createRomanMap('I', 'V', 'X').get(roman_1, 0)
    tens = createRomanMap('X', 'L', 'C').get(roman_10, 0)
    hundreds = createRomanMap('C', 'D', 'M').get(roman_100, 0)
    thousands = createRomanMap('M', '_', '__').get(roman_1000, 0)
    
    digits = [thousands, hundreds, tens, ones]
    return int(''.join([str(x) for x in digits]))