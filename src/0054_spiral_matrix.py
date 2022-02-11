def spiralOrder(matrix: list[list[int]]) -> list[int]:
    m, n = len(matrix) - 1, len(matrix[0])
    x, y = 0, 0
    result = []
    x_dir = 1
    y_dir = 1
    while m != -1 and n != 0:
        y_target = y + (y_dir * n)
        result.extend([matrix[x][_y] for _y in range(y, y_target, y_dir)])
        y = y_target - y_dir
        y_dir = -y_dir
        x += x_dir
        n -= 1
        
        x_target = x + (x_dir * m)
        result.extend([matrix[_x][y] for _x in range(x, x_target, x_dir)])
        x = x_target - x_dir
        x_dir = -x_dir
        y += y_dir
        m -= 1

    return result