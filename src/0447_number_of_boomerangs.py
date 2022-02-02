def numberOfBoomerangs(points: list[list[int]]) -> int:
    def dist_metric(a, b):
        return (a[0] - b[0])**2 + (a[1] - b[1])**2
    
    n = len(points)
    
    total = 0
    for i in range(n):
        counts = {}
        for j in range(n):
            if i == j:
                continue
            metric = dist_metric(points[i], points[j])
            counts[metric] = counts.get(metric, 0) + 1
        total += sum([math.perm(v, 2) for v in counts.values() if v > 1])
            
    return total