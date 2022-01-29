def removeStones(points):
    uf = {}
    num_roots = 0
    def find(x):
        nonlocal num_roots
        if x not in uf:
            uf[x] = x
            num_roots += 1
        if x != uf[x]:
            uf[x] = find(uf[x])
        return uf[x]
    for i, j in points:
        i_root = find(i)
        j_root = find(-j)
        if i_root != j_root:
            uf[i_root] = j_root
            num_roots -= 1
    return num_roots


print(removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))