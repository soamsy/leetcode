def findCircleNum(isConnected: list[list[int]]) -> int:
    n = len(isConnected)
    
    visited = [0] * n
    def dfs(i):
        if visited[i]:
            return 0
        visited[i] = 1
        
        for j, connection in enumerate(isConnected[i]):
            if connection == 1 and i != j:
                dfs(j)
        
        return 1
    
    return sum([dfs(i) for i in range(n)])