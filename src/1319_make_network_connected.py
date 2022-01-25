def makeConnected(n: int, connections: list[list[int]]) -> int:
    if len(connections) < n - 1:
        return -1
    
    networks = { i: {i} for i in range(n)}
    for a, b in connections:
        if networks[a] is networks[b]:
            continue
        
        networks[a].update(networks[b])
        for comp in networks[b]:
            networks[comp] = networks[a]
    
    network_count = 0
    unique_networks = set()
    for _, network in networks.items():
        size_before = len(unique_networks)
        unique_networks.update(network)
        if size_before < len(unique_networks):
            network_count += 1

    return network_count - 1