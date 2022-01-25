def minFlips(a: int, b: int, c: int) -> int:
    def bitcount(num):
        return len([n for n in str(bin(num)) if n == '1'])
    
    return bitcount((a | b) ^ c) + bitcount(a & b & ((a | b) ^ c))