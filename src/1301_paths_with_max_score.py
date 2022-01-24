def pathsWithMaxScore(board: list[str]) -> list[int]:
    m, n = len(board), len(board[0])
    MOD = 10**9 + 7
    
    dp = [[(0,0)] * n for _ in range(m)]
    
    dp[m-1][n-1] = (0, 1)
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if board[i][j] == 'X':
                continue
                
            options = []
            down = i + 1
            right = j + 1
            
            if down < m and board[down][j] != 'X':
                options.append(dp[down][j])
            if right < n and board[i][right] != 'X':
                options.append(dp[i][j+1])
            if down < m and right < n and board[down][right] != 'X':
                options.append(dp[down][right])
            
            if not options:
                continue
            most_money = max(options, key=lambda x: x[0])[0]
            paths = sum([op[1] for op in options if op[0] == most_money])
            if paths == 0:
                continue
            board_money = 0
            if board[i][j] not in {'E','S','X'}:
                board_money = int(board[i][j])
            dp[i][j] = (most_money + board_money, paths % MOD)
    
    return list(dp[0][0])