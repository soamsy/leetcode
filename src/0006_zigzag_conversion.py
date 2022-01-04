def convert(s, numRows):
    if numRows <= 1:
        return s
    col = 0
    i = 0
    grid = []
    while i < len(s):
        cycle = col % (numRows - 1) 
        if cycle == 0:
            seq = list(s[i:i+numRows])
            padding = [None] * (numRows - len(seq))
            seq = seq + padding
            grid.append(seq)
            i += numRows
        else:
            seq = [None] * numRows
            seq[-cycle-1] = s[i:i+1]
            grid.append(seq)
            i += 1
        col += 1
    
            
    flipped = list(map(lambda *x: list(x), *grid))
    return ''.join([''.join(filter(lambda el:el, row)) for row in flipped])


# print(convert("PAYPALISHIRING", 4))